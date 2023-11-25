# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_star.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_star.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18steammessages_star.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\xc6\x01\n\x13\x43STAR_KeyValueQuery\x12\x43\n\x03key\x18\x01 \x01(\tB6\x82\xb5\x18\x32key to search for in JSON path format (SQL subset)\x12j\n\x05value\x18\x02 \x01(\tB[\x82\xb5\x18Wthe value to compare against (the JSON value will be compared for equality as a string)\"\xcb\x01\n\x16\x43STAR_GlyphQueryParams\x12s\n\tbundle_id\x18\x01 \x01(\x04\x42`\x82\xb5\x18\\if provided, Bundle ID is used instead of the other query parameters (much faster SQL query)\x12<\n\x07queries\x18\x02 \x03(\x0b\x32\x14.CSTAR_KeyValueQueryB\x15\x82\xb5\x18\x11key value queries\"\x94\x02\n\x1b\x43STAR_ReadGlyphData_Request\x12\x65\n\x0cquery_params\x18\x01 \x01(\x0b\x32\x17.CSTAR_GlyphQueryParamsB6\x82\xb5\x18\x32parameters to identify the glyphs to read from SQL\x12\x8d\x01\n\x1elast_modified_time_lower_limit\x18\x02 \x01(\tBe\x82\xb5\x18\x61if provided, only return glyphs modified more recently than this timestamp  (RFC 3339 UTC format)\"\xec\x01\n\x0f\x43STAR_GlyphData\x12<\n\nglyph_guid\x18\x01 \x01(\x0c\x42(\x82\xb5\x18$GUID uniquely identifying this glyph\x12\x65\n\x13glyph_last_modified\x18\x02 \x01(\tBH\x82\xb5\x18\x44timestamp of when this glyph was last modified (RFC 3339 UTC format)\x12\x34\n\x0fglyph_json_data\x18\x03 \x01(\tB\x1b\x82\xb5\x18\x17JSON encoded glyph data\"\xb4\x01\n\x1c\x43STAR_WriteGlyphData_Request\x12@\n\tbundle_id\x18\x01 \x01(\x04\x42-\x82\xb5\x18)the Bundle ID of the glyphs to be written\x12R\n\nglyph_data\x18\x02 \x03(\x0b\x32\x10.CSTAR_GlyphDataB,\x82\xb5\x18(one or more items of glyph data to write\"\x7f\n\rCSTAR_Request\x12\x35\n\x0fread_glyph_data\x18\x01 \x01(\x0b\x32\x1c.CSTAR_ReadGlyphData_Request\x12\x37\n\x10write_glyph_data\x18\x02 \x01(\x0b\x32\x1d.CSTAR_WriteGlyphData_Request\"\xf1\x01\n\x1c\x43STAR_ReadGlyphData_Response\x12|\n\tbundle_id\x18\x01 \x01(\x04\x42i\x82\xb5\x18\x65the Bundle ID of the returned glyphs; the client should send this back to optimize subsequent queries\x12S\n\nglyph_data\x18\x02 \x03(\x0b\x32\x10.CSTAR_GlyphDataB-\x82\xb5\x18)zero or more items of returned glyph data\"w\n\x1d\x43STAR_WriteGlyphData_Response\x12V\n\x06result\x18\x01 \x03(\x0e\x32\x18.E_STAR_GlyphWriteResultB,\x82\xb5\x18(write result for each item of glyph data\"\x82\x01\n\x0e\x43STAR_Response\x12\x36\n\x0fread_glyph_data\x18\x01 \x01(\x0b\x32\x1d.CSTAR_ReadGlyphData_Response\x12\x38\n\x10write_glyph_data\x18\x02 \x01(\x0b\x32\x1e.CSTAR_WriteGlyphData_Response*\xc1\x01\n\x17\x45_STAR_GlyphWriteResult\x12%\n!k_E_STAR_GlyphWriteResult_Success\x10\x00\x12,\n(k_E_STAR_GlyphWriteResult_InvalidMessage\x10\x01\x12)\n%k_E_STAR_GlyphWriteResult_InvalidJSON\x10\x02\x12&\n\"k_E_STAR_GlyphWriteResult_SQLError\x10\x03\x32\x85\x01\n\x04STAR\x12R\n\x0eProcessMessage\x12\x0e.CSTAR_Request\x1a\x0f.CSTAR_Response\"\x1f\x82\xb5\x18\x1bprocesses a generic message\x1a)\x82\xb5\x18%service for reading/writing STAR dataB\x03\x90\x01\x01'
  ,
  dependencies=[steammessages__base__pb2.DESCRIPTOR,steammessages__unified__base__pb2.DESCRIPTOR,])

_E_STAR_GLYPHWRITERESULT = _descriptor.EnumDescriptor(
  name='E_STAR_GlyphWriteResult',
  full_name='E_STAR_GlyphWriteResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_E_STAR_GlyphWriteResult_Success', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_E_STAR_GlyphWriteResult_InvalidMessage', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_E_STAR_GlyphWriteResult_InvalidJSON', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_E_STAR_GlyphWriteResult_SQLError', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1824,
  serialized_end=2017,
)
_sym_db.RegisterEnumDescriptor(_E_STAR_GLYPHWRITERESULT)

E_STAR_GlyphWriteResult = enum_type_wrapper.EnumTypeWrapper(_E_STAR_GLYPHWRITERESULT)
k_E_STAR_GlyphWriteResult_Success = 0
k_E_STAR_GlyphWriteResult_InvalidMessage = 1
k_E_STAR_GlyphWriteResult_InvalidJSON = 2
k_E_STAR_GlyphWriteResult_SQLError = 3



_CSTAR_KEYVALUEQUERY = _descriptor.Descriptor(
  name='CSTAR_KeyValueQuery',
  full_name='CSTAR_KeyValueQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CSTAR_KeyValueQuery.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\0302key to search for in JSON path format (SQL subset)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='CSTAR_KeyValueQuery.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030Wthe value to compare against (the JSON value will be compared for equality as a string)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=89,
  serialized_end=287,
)


_CSTAR_GLYPHQUERYPARAMS = _descriptor.Descriptor(
  name='CSTAR_GlyphQueryParams',
  full_name='CSTAR_GlyphQueryParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='CSTAR_GlyphQueryParams.bundle_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\\if provided, Bundle ID is used instead of the other query parameters (much faster SQL query)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queries', full_name='CSTAR_GlyphQueryParams.queries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\021key value queries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=290,
  serialized_end=493,
)


_CSTAR_READGLYPHDATA_REQUEST = _descriptor.Descriptor(
  name='CSTAR_ReadGlyphData_Request',
  full_name='CSTAR_ReadGlyphData_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_params', full_name='CSTAR_ReadGlyphData_Request.query_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\0302parameters to identify the glyphs to read from SQL', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_modified_time_lower_limit', full_name='CSTAR_ReadGlyphData_Request.last_modified_time_lower_limit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030aif provided, only return glyphs modified more recently than this timestamp  (RFC 3339 UTC format)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=496,
  serialized_end=772,
)


_CSTAR_GLYPHDATA = _descriptor.Descriptor(
  name='CSTAR_GlyphData',
  full_name='CSTAR_GlyphData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='glyph_guid', full_name='CSTAR_GlyphData.glyph_guid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030$GUID uniquely identifying this glyph', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glyph_last_modified', full_name='CSTAR_GlyphData.glyph_last_modified', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030Dtimestamp of when this glyph was last modified (RFC 3339 UTC format)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glyph_json_data', full_name='CSTAR_GlyphData.glyph_json_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\027JSON encoded glyph data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=775,
  serialized_end=1011,
)


_CSTAR_WRITEGLYPHDATA_REQUEST = _descriptor.Descriptor(
  name='CSTAR_WriteGlyphData_Request',
  full_name='CSTAR_WriteGlyphData_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='CSTAR_WriteGlyphData_Request.bundle_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030)the Bundle ID of the glyphs to be written', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glyph_data', full_name='CSTAR_WriteGlyphData_Request.glyph_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030(one or more items of glyph data to write', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1014,
  serialized_end=1194,
)


_CSTAR_REQUEST = _descriptor.Descriptor(
  name='CSTAR_Request',
  full_name='CSTAR_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_glyph_data', full_name='CSTAR_Request.read_glyph_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='write_glyph_data', full_name='CSTAR_Request.write_glyph_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1196,
  serialized_end=1323,
)


_CSTAR_READGLYPHDATA_RESPONSE = _descriptor.Descriptor(
  name='CSTAR_ReadGlyphData_Response',
  full_name='CSTAR_ReadGlyphData_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='CSTAR_ReadGlyphData_Response.bundle_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030ethe Bundle ID of the returned glyphs; the client should send this back to optimize subsequent queries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glyph_data', full_name='CSTAR_ReadGlyphData_Response.glyph_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030)zero or more items of returned glyph data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1326,
  serialized_end=1567,
)


_CSTAR_WRITEGLYPHDATA_RESPONSE = _descriptor.Descriptor(
  name='CSTAR_WriteGlyphData_Response',
  full_name='CSTAR_WriteGlyphData_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CSTAR_WriteGlyphData_Response.result', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030(write result for each item of glyph data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1569,
  serialized_end=1688,
)


_CSTAR_RESPONSE = _descriptor.Descriptor(
  name='CSTAR_Response',
  full_name='CSTAR_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_glyph_data', full_name='CSTAR_Response.read_glyph_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='write_glyph_data', full_name='CSTAR_Response.write_glyph_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1691,
  serialized_end=1821,
)

_CSTAR_GLYPHQUERYPARAMS.fields_by_name['queries'].message_type = _CSTAR_KEYVALUEQUERY
_CSTAR_READGLYPHDATA_REQUEST.fields_by_name['query_params'].message_type = _CSTAR_GLYPHQUERYPARAMS
_CSTAR_WRITEGLYPHDATA_REQUEST.fields_by_name['glyph_data'].message_type = _CSTAR_GLYPHDATA
_CSTAR_REQUEST.fields_by_name['read_glyph_data'].message_type = _CSTAR_READGLYPHDATA_REQUEST
_CSTAR_REQUEST.fields_by_name['write_glyph_data'].message_type = _CSTAR_WRITEGLYPHDATA_REQUEST
_CSTAR_READGLYPHDATA_RESPONSE.fields_by_name['glyph_data'].message_type = _CSTAR_GLYPHDATA
_CSTAR_WRITEGLYPHDATA_RESPONSE.fields_by_name['result'].enum_type = _E_STAR_GLYPHWRITERESULT
_CSTAR_RESPONSE.fields_by_name['read_glyph_data'].message_type = _CSTAR_READGLYPHDATA_RESPONSE
_CSTAR_RESPONSE.fields_by_name['write_glyph_data'].message_type = _CSTAR_WRITEGLYPHDATA_RESPONSE
DESCRIPTOR.message_types_by_name['CSTAR_KeyValueQuery'] = _CSTAR_KEYVALUEQUERY
DESCRIPTOR.message_types_by_name['CSTAR_GlyphQueryParams'] = _CSTAR_GLYPHQUERYPARAMS
DESCRIPTOR.message_types_by_name['CSTAR_ReadGlyphData_Request'] = _CSTAR_READGLYPHDATA_REQUEST
DESCRIPTOR.message_types_by_name['CSTAR_GlyphData'] = _CSTAR_GLYPHDATA
DESCRIPTOR.message_types_by_name['CSTAR_WriteGlyphData_Request'] = _CSTAR_WRITEGLYPHDATA_REQUEST
DESCRIPTOR.message_types_by_name['CSTAR_Request'] = _CSTAR_REQUEST
DESCRIPTOR.message_types_by_name['CSTAR_ReadGlyphData_Response'] = _CSTAR_READGLYPHDATA_RESPONSE
DESCRIPTOR.message_types_by_name['CSTAR_WriteGlyphData_Response'] = _CSTAR_WRITEGLYPHDATA_RESPONSE
DESCRIPTOR.message_types_by_name['CSTAR_Response'] = _CSTAR_RESPONSE
DESCRIPTOR.enum_types_by_name['E_STAR_GlyphWriteResult'] = _E_STAR_GLYPHWRITERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CSTAR_KeyValueQuery = _reflection.GeneratedProtocolMessageType('CSTAR_KeyValueQuery', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_KEYVALUEQUERY,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_KeyValueQuery)
  })
_sym_db.RegisterMessage(CSTAR_KeyValueQuery)

CSTAR_GlyphQueryParams = _reflection.GeneratedProtocolMessageType('CSTAR_GlyphQueryParams', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_GLYPHQUERYPARAMS,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_GlyphQueryParams)
  })
_sym_db.RegisterMessage(CSTAR_GlyphQueryParams)

CSTAR_ReadGlyphData_Request = _reflection.GeneratedProtocolMessageType('CSTAR_ReadGlyphData_Request', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_READGLYPHDATA_REQUEST,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_ReadGlyphData_Request)
  })
_sym_db.RegisterMessage(CSTAR_ReadGlyphData_Request)

CSTAR_GlyphData = _reflection.GeneratedProtocolMessageType('CSTAR_GlyphData', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_GLYPHDATA,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_GlyphData)
  })
_sym_db.RegisterMessage(CSTAR_GlyphData)

CSTAR_WriteGlyphData_Request = _reflection.GeneratedProtocolMessageType('CSTAR_WriteGlyphData_Request', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_WRITEGLYPHDATA_REQUEST,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_WriteGlyphData_Request)
  })
_sym_db.RegisterMessage(CSTAR_WriteGlyphData_Request)

CSTAR_Request = _reflection.GeneratedProtocolMessageType('CSTAR_Request', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_REQUEST,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_Request)
  })
_sym_db.RegisterMessage(CSTAR_Request)

CSTAR_ReadGlyphData_Response = _reflection.GeneratedProtocolMessageType('CSTAR_ReadGlyphData_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_READGLYPHDATA_RESPONSE,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_ReadGlyphData_Response)
  })
_sym_db.RegisterMessage(CSTAR_ReadGlyphData_Response)

CSTAR_WriteGlyphData_Response = _reflection.GeneratedProtocolMessageType('CSTAR_WriteGlyphData_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_WRITEGLYPHDATA_RESPONSE,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_WriteGlyphData_Response)
  })
_sym_db.RegisterMessage(CSTAR_WriteGlyphData_Response)

CSTAR_Response = _reflection.GeneratedProtocolMessageType('CSTAR_Response', (_message.Message,), {
  'DESCRIPTOR' : _CSTAR_RESPONSE,
  '__module__' : 'steammessages_star_pb2'
  # @@protoc_insertion_point(class_scope:CSTAR_Response)
  })
_sym_db.RegisterMessage(CSTAR_Response)


DESCRIPTOR._options = None
_CSTAR_KEYVALUEQUERY.fields_by_name['key']._options = None
_CSTAR_KEYVALUEQUERY.fields_by_name['value']._options = None
_CSTAR_GLYPHQUERYPARAMS.fields_by_name['bundle_id']._options = None
_CSTAR_GLYPHQUERYPARAMS.fields_by_name['queries']._options = None
_CSTAR_READGLYPHDATA_REQUEST.fields_by_name['query_params']._options = None
_CSTAR_READGLYPHDATA_REQUEST.fields_by_name['last_modified_time_lower_limit']._options = None
_CSTAR_GLYPHDATA.fields_by_name['glyph_guid']._options = None
_CSTAR_GLYPHDATA.fields_by_name['glyph_last_modified']._options = None
_CSTAR_GLYPHDATA.fields_by_name['glyph_json_data']._options = None
_CSTAR_WRITEGLYPHDATA_REQUEST.fields_by_name['bundle_id']._options = None
_CSTAR_WRITEGLYPHDATA_REQUEST.fields_by_name['glyph_data']._options = None
_CSTAR_READGLYPHDATA_RESPONSE.fields_by_name['bundle_id']._options = None
_CSTAR_READGLYPHDATA_RESPONSE.fields_by_name['glyph_data']._options = None
_CSTAR_WRITEGLYPHDATA_RESPONSE.fields_by_name['result']._options = None

_STAR = _descriptor.ServiceDescriptor(
  name='STAR',
  full_name='STAR',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\265\030%service for reading/writing STAR data',
  create_key=_descriptor._internal_create_key,
  serialized_start=2020,
  serialized_end=2153,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessMessage',
    full_name='STAR.ProcessMessage',
    index=0,
    containing_service=None,
    input_type=_CSTAR_REQUEST,
    output_type=_CSTAR_RESPONSE,
    serialized_options=b'\202\265\030\033processes a generic message',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STAR)

DESCRIPTOR.services_by_name['STAR'] = _STAR

STAR = service_reflection.GeneratedServiceType('STAR', (_service.Service,), dict(
  DESCRIPTOR = _STAR,
  __module__ = 'steammessages_star_pb2'
  ))

STAR_Stub = service_reflection.GeneratedServiceStubType('STAR_Stub', (STAR,), dict(
  DESCRIPTOR = _STAR,
  __module__ = 'steammessages_star_pb2'
  ))


# @@protoc_insertion_point(module_scope)
