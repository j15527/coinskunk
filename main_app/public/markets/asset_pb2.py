# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='asset.proto',
  package='ProtobufMarkets',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x61sset.proto\x12\x0fProtobufMarkets\"o\n\x12\x41ssetUpdateMessage\x12\r\n\x05\x61sset\x18\x01 \x01(\x05\x12@\n\x0fusdVolumeUpdate\x18\x02 \x01(\x0b\x32%.ProtobufMarkets.AssetUSDVolumeUpdateH\x00\x42\x08\n\x06Update\"&\n\x14\x41ssetUSDVolumeUpdate\x12\x0e\n\x06volume\x18\x01 \x01(\tb\x06proto3')
)




_ASSETUPDATEMESSAGE = _descriptor.Descriptor(
  name='AssetUpdateMessage',
  full_name='ProtobufMarkets.AssetUpdateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='ProtobufMarkets.AssetUpdateMessage.asset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usdVolumeUpdate', full_name='ProtobufMarkets.AssetUpdateMessage.usdVolumeUpdate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Update', full_name='ProtobufMarkets.AssetUpdateMessage.Update',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=32,
  serialized_end=143,
)


_ASSETUSDVOLUMEUPDATE = _descriptor.Descriptor(
  name='AssetUSDVolumeUpdate',
  full_name='ProtobufMarkets.AssetUSDVolumeUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='ProtobufMarkets.AssetUSDVolumeUpdate.volume', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=183,
)

_ASSETUPDATEMESSAGE.fields_by_name['usdVolumeUpdate'].message_type = _ASSETUSDVOLUMEUPDATE
_ASSETUPDATEMESSAGE.oneofs_by_name['Update'].fields.append(
  _ASSETUPDATEMESSAGE.fields_by_name['usdVolumeUpdate'])
_ASSETUPDATEMESSAGE.fields_by_name['usdVolumeUpdate'].containing_oneof = _ASSETUPDATEMESSAGE.oneofs_by_name['Update']
DESCRIPTOR.message_types_by_name['AssetUpdateMessage'] = _ASSETUPDATEMESSAGE
DESCRIPTOR.message_types_by_name['AssetUSDVolumeUpdate'] = _ASSETUSDVOLUMEUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetUpdateMessage = _reflection.GeneratedProtocolMessageType('AssetUpdateMessage', (_message.Message,), dict(
  DESCRIPTOR = _ASSETUPDATEMESSAGE,
  __module__ = 'asset_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.AssetUpdateMessage)
  ))
_sym_db.RegisterMessage(AssetUpdateMessage)

AssetUSDVolumeUpdate = _reflection.GeneratedProtocolMessageType('AssetUSDVolumeUpdate', (_message.Message,), dict(
  DESCRIPTOR = _ASSETUSDVOLUMEUPDATE,
  __module__ = 'asset_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.AssetUSDVolumeUpdate)
  ))
_sym_db.RegisterMessage(AssetUSDVolumeUpdate)


# @@protoc_insertion_point(module_scope)
