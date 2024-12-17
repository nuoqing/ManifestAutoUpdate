import logging
import time

import requests
import hashlib
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - Line:%(lineno)s')

dirID = 0


def open_request(path, data, token, method='POST'):
    url = 'https://open-api.123pan.com' + path
    headers = {
        'Content-Type': 'application/json',
        'Platform': 'open_platform',
        'Authorization': 'Bearer ' + token
    }
    if method == 'POST':
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        if 'code' not in response_json or response_json['code'] != 0:
            raise Exception(response_json.get('message', '网络错误'))
        return response_json.get('data')
    else:
        response = requests.get(url, data=data, headers=headers)
        response_json = response.json()
        if 'code' not in response_json or response_json['code'] != 0:
            raise Exception(response_json.get('message', '网络错误'))
        return response_json.get('data')


# 上传分片
def put_part(url, part_stream, part_size):
    headers = {
        'Content-Length': str(part_size)
    }
    response = requests.put(url, data=part_stream, headers=headers)
    if response.status_code != 200:
        raise Exception(f'分片传输错误，错误码：{response.status_code}，错误信息：{response.text}')


# 创建文件夹
def create_folder(folder_name, parentID, token):
    res_data = open_request('/api/v1/access_token', {'clientID': client_id, 'clientSecret': client_secret}, token)
    token = res_data['accessToken']
    res_data = open_request('/upload/v1/file/mkdir', {'name': folder_name, 'parentID': parentID}, token)
    if res_data.get('dirID'):
        global dirID
        dirID = res_data['dirID']
        return res_data['dirID']
    else:
        raise Exception(f'创建文件夹失败，错误信息：{res_data.get("message")}')


# 上传文件
def upload_file(client_id, client_secret, folder_name, file_path,flag,getKey):
    if getKey:
        parent = 4134532
    else:
        parent = 4134530
    token = ''
    try:
        res_data = open_request('/api/v1/access_token', {'clientID': client_id, 'clientSecret': client_secret}, token)
        token = res_data['accessToken']
        # 开始创建文件夹
        try:
            if flag:
                create_folder(folder_name, parent, token)
            else:
                logging.info(f"无需创建 {folder_name}")
        except:
            logging.info(f"文件创建失败 {folder_name}")
        filename = os.path.basename(file_path).replace("_cache","")
        file_size = os.path.getsize(file_path)
        if getKey:
            with open(file_path, 'rb') as file:
                file_etag = hashlib.md5(file.read()).hexdigest()
            res_data = open_request('/upload/v1/file/create', {
                'parentFileID': 4134532,
                'filename': filename,
                'etag': file_etag,
                'size': file_size
            }, token)
        else:
            with open(file_path, 'rb') as file:
                file_etag = hashlib.md5(file.read()).hexdigest()
            res_data = open_request('/upload/v1/file/create', {
                'parentFileID': dirID,
                'filename': filename,
                'etag': file_etag,
                'size': file_size
            }, token)

        if res_data.get('reuse'):
            logging.info(f"极速上传成功 {filename} - {parent}")
            return

        upload_id = res_data['preuploadID']
        slice_size = res_data['sliceSize']
        res_data = open_request('/upload/v1/file/list_upload_parts', {'preuploadID': upload_id}, token)
        parts_map = {part['partNumber']: {'size': part['size'], 'etag': part['etag']} for part in res_data['parts']}

        with open(file_path, 'rb') as file:
            for i in range(0, file_size, slice_size):
                part_num = i // slice_size + 1
                temp_stream = file.read(slice_size)

                if part_num in parts_map and parts_map[part_num]['size'] == len(temp_stream) and parts_map[part_num][
                    'etag'] == hashlib.md5(temp_stream).hexdigest():
                    continue

                res_data = open_request('/upload/v1/file/get_upload_url',
                                        {'preuploadID': upload_id, 'sliceNo': part_num}, token)
                put_part(res_data['presignedURL'], temp_stream, len(temp_stream))

        res_data = open_request('/upload/v1/file/upload_complete', {'preuploadID': upload_id}, token)
        if res_data.get('completed'):
            logging.info(f"上传成功 {filename} - {parent}")
            return

        for j in range(200):
            time.sleep(5)
            res_data = open_request('/upload/v1/file/upload_async_result',
                                    {'parentFileID': parent}, token)
            if res_data.get('completed'):
                logging.info(f"上传成功 {filename} - {parent}")
                return

        logging.info("上传超时")

    except Exception as e:
        logging.info(f"上传失败: {e} - {file_path}")


client_id = 'a7a437c9b93e4667b7fdf46ef7e912cb'
client_secret = '6c09be6b4ef44406808eba1abd0d6222' 
#parent_file_id = 4119655  # 上传到的父级目录id，根目录为0
#local_file_path = 'C:\\Users\\44615\\PycharmProjects\\Demo_Pan\\data\\depots\\1000360\\1000360.txt'


def upload_file_pan(app_id,file_path,flag,getKey):
    upload_file(client_id, client_secret, app_id, file_path,flag,getKey)
