# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Progress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Progress.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eProgress.proto\"\x19\n\x08Progress\x12\r\n\x05value\x18\x01 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROGRESS = _descriptor.Descriptor(
  name='Progress',
  full_name='Progress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Progress.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=43,
)

DESCRIPTOR.message_types_by_name['Progress'] = _PROGRESS

Progress = _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), dict(
  DESCRIPTOR = _PROGRESS,
  __module__ = 'Progress_pb2'
  # @@protoc_insertion_point(class_scope:Progress)
  ))
_sym_db.RegisterMessage(Progress)


# @@protoc_insertion_point(module_scope)