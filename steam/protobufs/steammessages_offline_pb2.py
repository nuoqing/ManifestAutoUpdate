# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_offline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2
import steam.protobufs.offline_ticket_pb2 as offline__ticket__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_offline.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bsteammessages_offline.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x14offline_ticket.proto\"V\n&COffline_GetOfflineLogonTicket_Request\x12\x10\n\x08priority\x18\x01 \x01(\r\x12\x1a\n\x12perform_encryption\x18\x02 \x01(\x08\"\x82\x01\n\'COffline_GetOfflineLogonTicket_Response\x12\x19\n\x11serialized_ticket\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12)\n\x10\x65ncrypted_ticket\x18\x03 \x01(\x0b\x32\x0f.Offline_Ticket\"0\n.COffline_GetUnsignedOfflineLogonTicket_Request\"O\n\x1b\x43Offline_OfflineLogonTicket\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x1d\n\x15rtime32_creation_time\x18\x02 \x01(\x07\"_\n/COffline_GetUnsignedOfflineLogonTicket_Response\x12,\n\x06ticket\x18\x01 \x01(\x0b\x32\x1c.COffline_OfflineLogonTicket2\xa3\x03\n\x07Offline\x12\xb5\x01\n\x15GetOfflineLogonTicket\x12\'.COffline_GetOfflineLogonTicket_Request\x1a(.COffline_GetOfflineLogonTicket_Response\"I\x82\xb5\x18\x45Get a serialized and signed offline logon ticket for the current user\x12\xc1\x01\n\x1dGetUnsignedOfflineLogonTicket\x12/.COffline_GetUnsignedOfflineLogonTicket_Request\x1a\x30.COffline_GetUnsignedOfflineLogonTicket_Response\"=\x82\xb5\x18\x39Get an unsigned offline logon ticket for the current user\x1a\x1c\x82\xb5\x18\x18Offline settings serviceB\x03\x90\x01\x01'
  ,
  dependencies=[steammessages__base__pb2.DESCRIPTOR,steammessages__unified__base__pb2.DESCRIPTOR,offline__ticket__pb2.DESCRIPTOR,])




_COFFLINE_GETOFFLINELOGONTICKET_REQUEST = _descriptor.Descriptor(
  name='COffline_GetOfflineLogonTicket_Request',
  full_name='COffline_GetOfflineLogonTicket_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='COffline_GetOfflineLogonTicket_Request.priority', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='perform_encryption', full_name='COffline_GetOfflineLogonTicket_Request.perform_encryption', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=199,
)


_COFFLINE_GETOFFLINELOGONTICKET_RESPONSE = _descriptor.Descriptor(
  name='COffline_GetOfflineLogonTicket_Response',
  full_name='COffline_GetOfflineLogonTicket_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_ticket', full_name='COffline_GetOfflineLogonTicket_Response.serialized_ticket', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='COffline_GetOfflineLogonTicket_Response.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encrypted_ticket', full_name='COffline_GetOfflineLogonTicket_Response.encrypted_ticket', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=332,
)


_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST = _descriptor.Descriptor(
  name='COffline_GetUnsignedOfflineLogonTicket_Request',
  full_name='COffline_GetUnsignedOfflineLogonTicket_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=382,
)


_COFFLINE_OFFLINELOGONTICKET = _descriptor.Descriptor(
  name='COffline_OfflineLogonTicket',
  full_name='COffline_OfflineLogonTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountid', full_name='COffline_OfflineLogonTicket.accountid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rtime32_creation_time', full_name='COffline_OfflineLogonTicket.rtime32_creation_time', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=463,
)


_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE = _descriptor.Descriptor(
  name='COffline_GetUnsignedOfflineLogonTicket_Response',
  full_name='COffline_GetUnsignedOfflineLogonTicket_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticket', full_name='COffline_GetUnsignedOfflineLogonTicket_Response.ticket', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=560,
)

_COFFLINE_GETOFFLINELOGONTICKET_RESPONSE.fields_by_name['encrypted_ticket'].message_type = offline__ticket__pb2._OFFLINE_TICKET
_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE.fields_by_name['ticket'].message_type = _COFFLINE_OFFLINELOGONTICKET
DESCRIPTOR.message_types_by_name['COffline_GetOfflineLogonTicket_Request'] = _COFFLINE_GETOFFLINELOGONTICKET_REQUEST
DESCRIPTOR.message_types_by_name['COffline_GetOfflineLogonTicket_Response'] = _COFFLINE_GETOFFLINELOGONTICKET_RESPONSE
DESCRIPTOR.message_types_by_name['COffline_GetUnsignedOfflineLogonTicket_Request'] = _COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST
DESCRIPTOR.message_types_by_name['COffline_OfflineLogonTicket'] = _COFFLINE_OFFLINELOGONTICKET
DESCRIPTOR.message_types_by_name['COffline_GetUnsignedOfflineLogonTicket_Response'] = _COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

COffline_GetOfflineLogonTicket_Request = _reflection.GeneratedProtocolMessageType('COffline_GetOfflineLogonTicket_Request', (_message.Message,), {
  'DESCRIPTOR' : _COFFLINE_GETOFFLINELOGONTICKET_REQUEST,
  '__module__' : 'steammessages_offline_pb2'
  # @@protoc_insertion_point(class_scope:COffline_GetOfflineLogonTicket_Request)
  })
_sym_db.RegisterMessage(COffline_GetOfflineLogonTicket_Request)

COffline_GetOfflineLogonTicket_Response = _reflection.GeneratedProtocolMessageType('COffline_GetOfflineLogonTicket_Response', (_message.Message,), {
  'DESCRIPTOR' : _COFFLINE_GETOFFLINELOGONTICKET_RESPONSE,
  '__module__' : 'steammessages_offline_pb2'
  # @@protoc_insertion_point(class_scope:COffline_GetOfflineLogonTicket_Response)
  })
_sym_db.RegisterMessage(COffline_GetOfflineLogonTicket_Response)

COffline_GetUnsignedOfflineLogonTicket_Request = _reflection.GeneratedProtocolMessageType('COffline_GetUnsignedOfflineLogonTicket_Request', (_message.Message,), {
  'DESCRIPTOR' : _COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST,
  '__module__' : 'steammessages_offline_pb2'
  # @@protoc_insertion_point(class_scope:COffline_GetUnsignedOfflineLogonTicket_Request)
  })
_sym_db.RegisterMessage(COffline_GetUnsignedOfflineLogonTicket_Request)

COffline_OfflineLogonTicket = _reflection.GeneratedProtocolMessageType('COffline_OfflineLogonTicket', (_message.Message,), {
  'DESCRIPTOR' : _COFFLINE_OFFLINELOGONTICKET,
  '__module__' : 'steammessages_offline_pb2'
  # @@protoc_insertion_point(class_scope:COffline_OfflineLogonTicket)
  })
_sym_db.RegisterMessage(COffline_OfflineLogonTicket)

COffline_GetUnsignedOfflineLogonTicket_Response = _reflection.GeneratedProtocolMessageType('COffline_GetUnsignedOfflineLogonTicket_Response', (_message.Message,), {
  'DESCRIPTOR' : _COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE,
  '__module__' : 'steammessages_offline_pb2'
  # @@protoc_insertion_point(class_scope:COffline_GetUnsignedOfflineLogonTicket_Response)
  })
_sym_db.RegisterMessage(COffline_GetUnsignedOfflineLogonTicket_Response)


DESCRIPTOR._options = None

_OFFLINE = _descriptor.ServiceDescriptor(
  name='Offline',
  full_name='Offline',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\265\030\030Offline settings service',
  create_key=_descriptor._internal_create_key,
  serialized_start=563,
  serialized_end=982,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOfflineLogonTicket',
    full_name='Offline.GetOfflineLogonTicket',
    index=0,
    containing_service=None,
    input_type=_COFFLINE_GETOFFLINELOGONTICKET_REQUEST,
    output_type=_COFFLINE_GETOFFLINELOGONTICKET_RESPONSE,
    serialized_options=b'\202\265\030EGet a serialized and signed offline logon ticket for the current user',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUnsignedOfflineLogonTicket',
    full_name='Offline.GetUnsignedOfflineLogonTicket',
    index=1,
    containing_service=None,
    input_type=_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_REQUEST,
    output_type=_COFFLINE_GETUNSIGNEDOFFLINELOGONTICKET_RESPONSE,
    serialized_options=b'\202\265\0309Get an unsigned offline logon ticket for the current user',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OFFLINE)

DESCRIPTOR.services_by_name['Offline'] = _OFFLINE

Offline = service_reflection.GeneratedServiceType('Offline', (_service.Service,), dict(
  DESCRIPTOR = _OFFLINE,
  __module__ = 'steammessages_offline_pb2'
  ))

Offline_Stub = service_reflection.GeneratedServiceStubType('Offline_Stub', (Offline,), dict(
  DESCRIPTOR = _OFFLINE,
  __module__ = 'steammessages_offline_pb2'
  ))


# @@protoc_insertion_point(module_scope)
