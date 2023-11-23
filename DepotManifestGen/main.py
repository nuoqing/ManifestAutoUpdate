import requests
import vdf
import gevent
import struct
import os.path
import logging
import argparse
import traceback
from pathlib import Path
from binascii import crc32
from six import itervalues, iteritems
from steam.client import SteamClient
from steam.client.cdn import CDNClient
from steam.enums import EResult, EType
from steam.exceptions import SteamError
from steam.protobufs.content_manifest_pb2 import ContentManifestSignature
from steam.utils.tools import *

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', required=True)
parser.add_argument('-p', '--password', required=False, default='')
parser.add_argument('-a', '--app-id', required=False)
parser.add_argument('-l', '--list-apps', action='store_true', required=False)
parser.add_argument('-s', '--sentry-path', '--ssfn', required=False)
parser.add_argument('-k', '--login-key', required=False)
parser.add_argument('-f', '--two-factor-code', required=False)
parser.add_argument('-A', '--auth-code', required=False)
parser.add_argument('-i', '--login-id', required=False)
parser.add_argument('-c', '--cli', action='store_true', required=False)
parser.add_argument('-L', '--level', required=False, default='INFO')
parser.add_argument('-C', '--credential-location', required=False)
parser.add_argument('-r', '--remove-old', action='store_true', required=False)


class BillingType:
    NoCost = 0
    BillOnceOnly = 1
    BillMonthly = 2
    ProofOfPrepurchaseOnly = 3
    GuestPass = 4
    HardwarePromo = 5
    Gift = 6
    AutoGrant = 7
    OEMTicket = 8
    RecurringOption = 9
    BillOnceOrCDKey = 10
    Repurchaseable = 11
    FreeOnDemand = 12
    Rental = 13
    CommercialLicense = 14
    FreeCommercialLicense = 15
    NumBillingTypes = 16
    PaidList = [BillOnceOnly, BillMonthly, BillOnceOrCDKey, Repurchaseable, Rental, ProofOfPrepurchaseOnly]


class Result(dict):
    def __init__(self, result=False, code=EResult.Fail, *args, **kwargs):
        super().__init__()
        self.result = result
        self.args = args
        self.code = code
        self.update(kwargs)

    def __bool__(self):
        return bool(self.result)


def get_manifest(save_id, cdn, app_id, depot_id, manifest_gid, remove_old=False, save_path=None, retry_num=10):
    if not save_path:
        save_path = Path().absolute()
    # app_path = save_path / f'depots/{app_id}'
    app_path = save_path / f'depots/{save_id}'
    manifest_path = app_path / f'{depot_id}_{manifest_gid}.manifest'
    if manifest_path.exists():
        return Result(result=True, code=EResult.OK, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid)
    while True:
        try:
            manifest_code = cdn.get_manifest_request_code(app_id, depot_id, manifest_gid)
            manifest = cdn.get_manifest(app_id, depot_id, manifest_gid, decrypt=False,
                                        manifest_request_code=manifest_code)
            depot_key = cdn.get_depot_key(manifest.app_id, manifest.depot_id)
            log.info(
                f"{cdn.get_manifest(app_id, depot_id, manifest_gid, decrypt=False, manifest_request_code=manifest_code)}")
            break
        except KeyboardInterrupt:
            exit(-1)
        except SteamError as e:
            if retry_num == 0:
                return Result(result=False, code=e.eresult, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid)
            retry_num -= 1
            log.warning(f'{e.message} result: {str(e.eresult)}')
            if e.eresult == EResult.AccessDenied:
                return Result(result=False, code=e.eresult, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid)
            gevent.idle()
        except:
            log.error(traceback.format_exc())
            return Result(result=False, code=EResult.Fail, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid)
    log.info(
        f'{"":<10}app_id: {app_id:<8}{"":<10}depot_id: {depot_id:<8}{"":<10}manifest_gid: {manifest_gid:20}{"":<10}DecryptionKey: {depot_key.hex()}')
    manifest.decrypt_filenames(depot_key)
    manifest.signature = ContentManifestSignature()
    for mapping in manifest.payload.mappings:
        mapping.filename = mapping.filename.rstrip('\x00 \n\t')
        mapping.chunks.sort(key=lambda x: x.sha)
    manifest.payload.mappings.sort(key=lambda x: x.filename.lower())
    if not os.path.exists(app_path):
        os.makedirs(app_path)
    if os.path.isfile(app_path / 'config.vdf'):
        with open(app_path / 'config.vdf') as f:
            d = vdf.load(f)
    else:
        d = vdf.VDFDict({'depots': {}})
    d['depots'][depot_id] = {'DecryptionKey': depot_key.hex()}
    d = {'depots': dict(sorted(d['depots'].items()))}
    delete_list = []
    if remove_old:
        for file in app_path.iterdir():
            if file.suffix == '.manifest':
                depot_id_, manifest_gid_ = file.stem.split('_')
                if depot_id_ == str(depot_id) and manifest_gid_ != str(manifest_gid):
                    file.unlink(missing_ok=True)
                    delete_list.append(file.name)
    buffer = manifest.payload.SerializeToString()
    manifest.metadata.crc_clear = crc32(struct.pack('<I', len(buffer)) + buffer)
    with open(manifest_path, 'wb') as f:
        f.write(manifest.serialize(compress=False))
    with open(app_path / 'config.vdf', 'w') as f:
        vdf.dump(d, f, pretty=True)
    # try:
    #     # addconfig = {}
    #     # if os.path.exists(app_path / 'addconfig.vdf'):
    #     #     print('***************************---addconfig')
    #     #     adc = vdf.load(open(app_path / 'addconfig.vdf'))
    #     #     addconfig = adc['depots']
    #     # for key in addconfig.keys():
    #     #     d['depots'][key] = addconfig[key]
    #     # with open(app_path / 'config.vdf', 'w') as f:
    #     #     vdf.dump(d, f, pretty=True)
    #
    #
    #     dkeys = getDecryptionKey(app_path / 'config.vdf')
    #     path = 'data/depots/' + str(app_id)
    #     if os.path.exists(path + '/' + 'iuser' + '.txt'):
    #         friuser = open(path + '/' + 'iuser' + '.txt', 'r', encoding='utf-8')
    #         iuser = friuser.readline()
    #         friuser.close()
    #     else:
    #         iuser = ''
    #
    #     frticket = open(path + '/' + str(app_id) + '-ticket' + '.txt', 'r', encoding='utf-8')
    #     ticket = frticket.readlines()
    #     frticket.close()
    #     filepathonly = path + '/' + str(app_id) + '-ticket-only.txt'
    #     fr = open(filepathonly, 'r', encoding='utf-8')
    #     flag = False
    #     onlys = fr.readlines()
    #     fr.close()
    #
    #     onlyticket = []
    #     ot = ''
    #     flagappid = False
    #     for line in onlys:
    #         line = line.strip()
    #         onlyts = line.split('----')
    #         if len(onlyts) == 2:
    #             ot = onlyts[1]
    #             onlyticket.append(onlyts[1])
    #             if onlyts[0] == str(app_id):
    #                 flagappid = True
    #     if len(set(onlyticket)) == 1:
    #         flag = True
    #     filepath = path + '/' + str(app_id) + '.txt'
    #     fw = open(filepath, 'w+', encoding='utf-8')
    #     fw.write(iuser + '\n')
    #     for item in dkeys:
    #         fw.write(item + '\n')
    #     for line in ticket:
    #         fw.write(line.strip() + '\n')
    #     if flag:
    #         fw.write(encrypt(str(app_id) + '----' + ot) + '\n')
    #     if not flagappid and len(onlyticket) > 0:
    #         fw.write(encrypt(str(app_id) + '----' + onlyticket[0]) + '\n')
    #
    #     fw.close()
    #
    #     fr = open(filepath, 'r', encoding='utf-8')
    #     tlines = fr.readlines()
    #     fr.close()
    #     tls = []
    #     fw = open(filepath, 'w+', encoding='utf-8')
    #     for line in tlines:
    #         if line not in tls:
    #             fw.write(line)
    #             tls.append(line)
    #     fw.close()
    #
    #     upload_aliyun('gKeyConfig/' + str(app_id) + '.txt', filepath)
    #     files = os.listdir(path)
    #     fw = open('temp.txt', 'w+', encoding='utf-8')
    #
    #     for file in files:
    #         if file.endswith('fest') or file.endswith('svd'):
    #             fw.write(file.split('.')[0] + '\n')
    #             upload_aliyun('depotcache/' + str(app_id) + '/' + file, path + '/' + file)
    #
    #     fw.close()
    #     upload_aliyun('depotcache/' + str(app_id) + '/' + str(app_id) + '.txt', 'temp.txt')
    #     log.info("--------------上传成功---------------")
    # except:
    #     log.error("--------------出错---------------")
    #     return Result(result=True, code=EResult.OK, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid,
    #                   delete_list=delete_list)

    return Result(result=True, code=EResult.OK, app_id=app_id, depot_id=depot_id, manifest_gid=manifest_gid,
                  delete_list=delete_list)


class MySteamClient(SteamClient):
    credential_location = str(Path('client').absolute())
    _LOG = logging.getLogger('MySteamClient')
    sentry_path = None
    login_key_path = None

    def __init__(self, credential_location=None, sentry_path=None):
        if credential_location:
            self.credential_location = credential_location
        if not Path(self.credential_location).exists():
            Path(self.credential_location).mkdir(parents=True, exist_ok=True)
        if sentry_path:
            if Path(sentry_path).exists():
                self.sentry_path = sentry_path
            elif (Path('client') / sentry_path).exists():
                self.sentry_path = str(Path('client') / sentry_path)
        SteamClient.__init__(self)

    def _handle_update_machine_auth(self, message):
        SteamClient._handle_update_machine_auth(self, message)

    def _handle_login_key(self, message):
        SteamClient._handle_login_key(self, message)
        with (Path(self.credential_location) / f'{self.username}.key').open('w') as f:
            f.write(self.login_key)

    def _handle_logon(self, msg):
        SteamClient._handle_logon(self, msg)

    def _get_sentry_path(self, username):
        if self.sentry_path:
            return self.sentry_path
        else:
            return SteamClient._get_sentry_path(self, username)

    def relogin(self):
        result = SteamClient.relogin(self)
        if result == EResult.InvalidPassword and self.login_key_path:
            self.login_key_path.unlink(missing_ok=True)
        return result

    def __setattr__(self, key, value):
        SteamClient.__setattr__(self, key, value)
        if key == 'username':
            if not self.login_key_path:
                self.login_key_path = Path(self.credential_location) / f'{self.username}.key'
                if not self.login_key and self.login_key_path.exists():
                    with self.login_key_path.open() as f:
                        self.login_key = f.read()


class MyCDNClient(CDNClient):
    _LOG = logging.getLogger('MyCDNClient')
    packages_info = None

    def load_licenses(self):
        """Read licenses from SteamClient instance, required for determining accessible content"""
        self.licensed_app_ids.clear()
        self.licensed_depot_ids.clear()

        if self.steam.steam_id.type == EType.AnonUser:
            packages = [17906]
        else:
            if not self.steam.licenses:
                self._LOG.debug("No steam licenses found on SteamClient instance")
                return

            packages = list(map(lambda l: {'packageid': l.package_id, 'access_token': l.access_token},
                                itervalues(self.steam.licenses)))

        self.packages_info = self.steam.get_product_info(packages=packages)['packages']

        for package_id, info in iteritems(self.packages_info):
            self.licensed_app_ids.update(info['appids'].values())
            self.licensed_depot_ids.update(info['depotids'].values())


log = logging.getLogger('DepotManifestGen')


def main(args=None):
    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()
    if args.level:
        level = logging.getLevelName(args.level.upper())
    else:
        level = logging.INFO
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=level)
    steam = MySteamClient(args.credential_location, args.sentry_path)
    steam.username = args.username
    if args.login_key:
        steam.login_key = args.login_key
    result = steam.relogin()
    if result != EResult.OK:
        if args.cli:
            result = steam.cli_login(args.username, args.password)
        else:
            result = steam.login(args.username, args.password, args.login_key, args.auth_code, args.two_factor_code,
                                 int(args.login_id) if args.login_id else None)
    if result != EResult.OK:
        log.error(f'Login failure reason: {result.__repr__()}')
        exit(result)
    app_id_list = []
    app_id_list_all = set()
    depot_id_list = []
    packages_info = []
    cdn = MyCDNClient(steam)
    if cdn.packages_info:
        for package_id, info in steam.get_product_info(packages=cdn.packages_info)['packages'].items():
            if 'depotids' in info and info['depotids'] and info['billingtype'] in BillingType.PaidList:
                app_id_list_all.update(list(info['appids'].values()))
                app_id_list.extend(list(info['appids'].values()))
                depot_id_list.extend(list(info['depotids'].values()))
                packages_info.append((list(info['appids'].values()), list(info['depotids'].values())))
    if args.app_id:
        app_id_list = {int(app_id) for app_id in args.app_id.split(',')}
        app_id_list_all.update(app_id_list)
    fresh_resp = steam.get_product_info(app_id_list)
    if args.list_apps:
        for app_id in app_id_list_all:
            app = fresh_resp['apps'][app_id]
            if 'common' in app and app['common']['type'].lower() in ['game', 'dlc', 'application']:
                log.info("%s | %s | %s", app_id, app['common']['type'].upper(), app['common']['name'])
        exit()
    result_list = []
    for app_id in app_id_list:
        app = fresh_resp['apps'][app_id]
        if 'common' in app and app['common']['type'].lower() in ['game', 'dlc', 'application']:
            if 'depots' not in fresh_resp['apps'][app_id]:
                continue
            for depot_id, depot in fresh_resp['apps'][app_id]['depots'].items():
                if 'manifests' in depot and 'public' in depot['manifests'] and int(
                        depot_id) in {*cdn.licensed_depot_ids, *cdn.licensed_app_ids}:
                    result_list.append(gevent.spawn(get_manifest, cdn, app_id, depot_id, depot['manifests']['public'],
                                                    args.remove_old))
                    gevent.idle()
    try:
        gevent.joinall(result_list)
    except KeyboardInterrupt:
        exit(-1)


if __name__ == '__main__':
    main()
    # old-gai
