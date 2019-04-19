# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndnrtc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ndnrtc.proto',
  package='ndnrtc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cndnrtc.proto\x12\x06ndnrtc\x1a\x1fgoogle/protobuf/timestamp.proto\"c\n\nStreamMeta\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\r\x12\x10\n\x08gop_size\x18\x05 \x01(\r\"\xe3\x01\n\x08LiveMeta\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tframerate\x18\x02 \x01(\x02\x12\x14\n\x0csegnum_delta\x18\x03 \x01(\x02\x12\x12\n\nsegnum_key\x18\x04 \x01(\x02\x12\x1b\n\x13segnum_delta_parity\x18\x05 \x01(\x02\x12\x19\n\x11segnum_key_parity\x18\x06 \x01(\x02\x12\x17\n\x0fsegnum_estimate\x18\x07 \x01(\x05\x12\x1a\n\x12\x66ramesize_estimate\x18\x08 \x01(\x05\"\x89\x02\n\tFrameMeta\x12\x13\n\x0bparity_size\x18\x01 \x01(\x05\x12\x14\n\x0cgop_position\x18\x02 \x01(\x05\x12\x12\n\ngop_number\x18\x03 \x01(\x05\x12\x35\n\x11\x63\x61pture_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10generation_delay\x18\x05 \x01(\x05\x12)\n\x04type\x18\x06 \x01(\x0e\x32\x1b.ndnrtc.FrameMeta.FrameType\x12\x13\n\x0b\x64\x61taseg_num\x18\x07 \x01(\x05\",\n\tFrameType\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05\x44\x65lta\x10\x01\x12\x07\n\x03Key\x10\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_FRAMEMETA_FRAMETYPE = _descriptor.EnumDescriptor(
  name='FrameType',
  full_name='ndnrtc.FrameMeta.FrameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Delta', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Key', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=610,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_FRAMEMETA_FRAMETYPE)


_STREAMMETA = _descriptor.Descriptor(
  name='StreamMeta',
  full_name='ndnrtc.StreamMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='ndnrtc.StreamMeta.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='ndnrtc.StreamMeta.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ndnrtc.StreamMeta.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitrate', full_name='ndnrtc.StreamMeta.bitrate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gop_size', full_name='ndnrtc.StreamMeta.gop_size', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=57,
  serialized_end=156,
)


_LIVEMETA = _descriptor.Descriptor(
  name='LiveMeta',
  full_name='ndnrtc.LiveMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ndnrtc.LiveMeta.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='framerate', full_name='ndnrtc.LiveMeta.framerate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segnum_delta', full_name='ndnrtc.LiveMeta.segnum_delta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segnum_key', full_name='ndnrtc.LiveMeta.segnum_key', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segnum_delta_parity', full_name='ndnrtc.LiveMeta.segnum_delta_parity', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segnum_key_parity', full_name='ndnrtc.LiveMeta.segnum_key_parity', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segnum_estimate', full_name='ndnrtc.LiveMeta.segnum_estimate', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='framesize_estimate', full_name='ndnrtc.LiveMeta.framesize_estimate', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=159,
  serialized_end=386,
)


_FRAMEMETA = _descriptor.Descriptor(
  name='FrameMeta',
  full_name='ndnrtc.FrameMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parity_size', full_name='ndnrtc.FrameMeta.parity_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gop_position', full_name='ndnrtc.FrameMeta.gop_position', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gop_number', full_name='ndnrtc.FrameMeta.gop_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capture_timestamp', full_name='ndnrtc.FrameMeta.capture_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation_delay', full_name='ndnrtc.FrameMeta.generation_delay', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ndnrtc.FrameMeta.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataseg_num', full_name='ndnrtc.FrameMeta.dataseg_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FRAMEMETA_FRAMETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=654,
)

_LIVEMETA.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FRAMEMETA.fields_by_name['capture_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FRAMEMETA.fields_by_name['type'].enum_type = _FRAMEMETA_FRAMETYPE
_FRAMEMETA_FRAMETYPE.containing_type = _FRAMEMETA
DESCRIPTOR.message_types_by_name['StreamMeta'] = _STREAMMETA
DESCRIPTOR.message_types_by_name['LiveMeta'] = _LIVEMETA
DESCRIPTOR.message_types_by_name['FrameMeta'] = _FRAMEMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamMeta = _reflection.GeneratedProtocolMessageType('StreamMeta', (_message.Message,), dict(
  DESCRIPTOR = _STREAMMETA,
  __module__ = 'ndnrtc_pb2'
  # @@protoc_insertion_point(class_scope:ndnrtc.StreamMeta)
  ))
_sym_db.RegisterMessage(StreamMeta)

LiveMeta = _reflection.GeneratedProtocolMessageType('LiveMeta', (_message.Message,), dict(
  DESCRIPTOR = _LIVEMETA,
  __module__ = 'ndnrtc_pb2'
  # @@protoc_insertion_point(class_scope:ndnrtc.LiveMeta)
  ))
_sym_db.RegisterMessage(LiveMeta)

FrameMeta = _reflection.GeneratedProtocolMessageType('FrameMeta', (_message.Message,), dict(
  DESCRIPTOR = _FRAMEMETA,
  __module__ = 'ndnrtc_pb2'
  # @@protoc_insertion_point(class_scope:ndnrtc.FrameMeta)
  ))
_sym_db.RegisterMessage(FrameMeta)


# @@protoc_insertion_point(module_scope)