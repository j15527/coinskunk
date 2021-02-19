# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pair.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pair.proto',
  package='ProtobufMarkets',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\npair.proto\x12\x0fProtobufMarkets\"\xe8\x01\n\x11PairUpdateMessage\x12\x0c\n\x04pair\x18\x01 \x01(\x04\x12\x35\n\nvwapUpdate\x18\x02 \x01(\x0b\x32\x1f.ProtobufMarkets.PairVwapUpdateH\x00\x12\x43\n\x11performanceUpdate\x18\x03 \x01(\x0b\x32&.ProtobufMarkets.PairPerformanceUpdateH\x00\x12?\n\x0ftrendlineUpdate\x18\x04 \x01(\x0b\x32$.ProtobufMarkets.PairTrendlineUpdateH\x00\x42\x08\n\x06Update\"H\n\x0ePairVwapUpdate\x12\x0c\n\x04vwap\x18\x01 \x01(\x01\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x15\n\rtimestampNano\x18\x03 \x01(\x03\"<\n\x15PairPerformanceUpdate\x12\x0e\n\x06window\x18\x01 \x01(\t\x12\x13\n\x0bperformance\x18\x02 \x01(\x01\"R\n\x13PairTrendlineUpdate\x12\x0e\n\x06window\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x03\x12\r\n\x05price\x18\x03 \x01(\t\x12\x0e\n\x06volume\x18\x04 \x01(\tb\x06proto3')
)




_PAIRUPDATEMESSAGE = _descriptor.Descriptor(
  name='PairUpdateMessage',
  full_name='ProtobufMarkets.PairUpdateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pair', full_name='ProtobufMarkets.PairUpdateMessage.pair', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vwapUpdate', full_name='ProtobufMarkets.PairUpdateMessage.vwapUpdate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performanceUpdate', full_name='ProtobufMarkets.PairUpdateMessage.performanceUpdate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trendlineUpdate', full_name='ProtobufMarkets.PairUpdateMessage.trendlineUpdate', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
      name='Update', full_name='ProtobufMarkets.PairUpdateMessage.Update',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=32,
  serialized_end=264,
)


_PAIRVWAPUPDATE = _descriptor.Descriptor(
  name='PairVwapUpdate',
  full_name='ProtobufMarkets.PairVwapUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vwap', full_name='ProtobufMarkets.PairVwapUpdate.vwap', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ProtobufMarkets.PairVwapUpdate.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestampNano', full_name='ProtobufMarkets.PairVwapUpdate.timestampNano', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=266,
  serialized_end=338,
)


_PAIRPERFORMANCEUPDATE = _descriptor.Descriptor(
  name='PairPerformanceUpdate',
  full_name='ProtobufMarkets.PairPerformanceUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='ProtobufMarkets.PairPerformanceUpdate.window', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performance', full_name='ProtobufMarkets.PairPerformanceUpdate.performance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=340,
  serialized_end=400,
)


_PAIRTRENDLINEUPDATE = _descriptor.Descriptor(
  name='PairTrendlineUpdate',
  full_name='ProtobufMarkets.PairTrendlineUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='ProtobufMarkets.PairTrendlineUpdate.window', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='ProtobufMarkets.PairTrendlineUpdate.time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='ProtobufMarkets.PairTrendlineUpdate.price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='ProtobufMarkets.PairTrendlineUpdate.volume', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=402,
  serialized_end=484,
)

_PAIRUPDATEMESSAGE.fields_by_name['vwapUpdate'].message_type = _PAIRVWAPUPDATE
_PAIRUPDATEMESSAGE.fields_by_name['performanceUpdate'].message_type = _PAIRPERFORMANCEUPDATE
_PAIRUPDATEMESSAGE.fields_by_name['trendlineUpdate'].message_type = _PAIRTRENDLINEUPDATE
_PAIRUPDATEMESSAGE.oneofs_by_name['Update'].fields.append(
  _PAIRUPDATEMESSAGE.fields_by_name['vwapUpdate'])
_PAIRUPDATEMESSAGE.fields_by_name['vwapUpdate'].containing_oneof = _PAIRUPDATEMESSAGE.oneofs_by_name['Update']
_PAIRUPDATEMESSAGE.oneofs_by_name['Update'].fields.append(
  _PAIRUPDATEMESSAGE.fields_by_name['performanceUpdate'])
_PAIRUPDATEMESSAGE.fields_by_name['performanceUpdate'].containing_oneof = _PAIRUPDATEMESSAGE.oneofs_by_name['Update']
_PAIRUPDATEMESSAGE.oneofs_by_name['Update'].fields.append(
  _PAIRUPDATEMESSAGE.fields_by_name['trendlineUpdate'])
_PAIRUPDATEMESSAGE.fields_by_name['trendlineUpdate'].containing_oneof = _PAIRUPDATEMESSAGE.oneofs_by_name['Update']
DESCRIPTOR.message_types_by_name['PairUpdateMessage'] = _PAIRUPDATEMESSAGE
DESCRIPTOR.message_types_by_name['PairVwapUpdate'] = _PAIRVWAPUPDATE
DESCRIPTOR.message_types_by_name['PairPerformanceUpdate'] = _PAIRPERFORMANCEUPDATE
DESCRIPTOR.message_types_by_name['PairTrendlineUpdate'] = _PAIRTRENDLINEUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PairUpdateMessage = _reflection.GeneratedProtocolMessageType('PairUpdateMessage', (_message.Message,), dict(
  DESCRIPTOR = _PAIRUPDATEMESSAGE,
  __module__ = 'pair_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.PairUpdateMessage)
  ))
_sym_db.RegisterMessage(PairUpdateMessage)

PairVwapUpdate = _reflection.GeneratedProtocolMessageType('PairVwapUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PAIRVWAPUPDATE,
  __module__ = 'pair_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.PairVwapUpdate)
  ))
_sym_db.RegisterMessage(PairVwapUpdate)

PairPerformanceUpdate = _reflection.GeneratedProtocolMessageType('PairPerformanceUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PAIRPERFORMANCEUPDATE,
  __module__ = 'pair_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.PairPerformanceUpdate)
  ))
_sym_db.RegisterMessage(PairPerformanceUpdate)

PairTrendlineUpdate = _reflection.GeneratedProtocolMessageType('PairTrendlineUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PAIRTRENDLINEUPDATE,
  __module__ = 'pair_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufMarkets.PairTrendlineUpdate)
  ))
_sym_db.RegisterMessage(PairTrendlineUpdate)


# @@protoc_insertion_point(module_scope)
