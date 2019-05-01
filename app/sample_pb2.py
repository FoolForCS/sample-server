# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csample.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"g\n\x06Sample\x12\n\n\x02id\x18\x01 \x01(\x03\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x10SampleCollection\x12\x18\n\x07samples\x18\x01 \x03(\x0b\x32\x07.Sample\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\"Q\n\x08\x41\x63tivity\x12\x0f\n\x07unknown\x18\x01 \x01(\x08\x12\x12\n\nstationary\x18\x02 \x01(\x08\x12\x0f\n\x07walking\x18\x03 \x01(\x08\x12\x0f\n\x07running\x18\x04 \x01(\x08\"/\n\x0c\x41\x63\x63\x65leration\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sample.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='Sample.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Sample.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=76,
  serialized_end=179,
)


_SAMPLECOLLECTION = _descriptor.Descriptor(
  name='SampleCollection',
  full_name='SampleCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='samples', full_name='SampleCollection.samples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=181,
  serialized_end=225,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=1,
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
  serialized_start=227,
  serialized_end=274,
)


_ACTIVITY = _descriptor.Descriptor(
  name='Activity',
  full_name='Activity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown', full_name='Activity.unknown', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stationary', full_name='Activity.stationary', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walking', full_name='Activity.walking', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running', full_name='Activity.running', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=276,
  serialized_end=357,
)


_ACCELERATION = _descriptor.Descriptor(
  name='Acceleration',
  full_name='Acceleration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Acceleration.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Acceleration.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='Acceleration.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=359,
  serialized_end=406,
)

_SAMPLE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SAMPLE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SAMPLECOLLECTION.fields_by_name['samples'].message_type = _SAMPLE
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['SampleCollection'] = _SAMPLECOLLECTION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Activity'] = _ACTIVITY
DESCRIPTOR.message_types_by_name['Acceleration'] = _ACCELERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Sample)
  ))
_sym_db.RegisterMessage(Sample)

SampleCollection = _reflection.GeneratedProtocolMessageType('SampleCollection', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLECOLLECTION,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:SampleCollection)
  ))
_sym_db.RegisterMessage(SampleCollection)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  ))
_sym_db.RegisterMessage(Location)

Activity = _reflection.GeneratedProtocolMessageType('Activity', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVITY,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Activity)
  ))
_sym_db.RegisterMessage(Activity)

Acceleration = _reflection.GeneratedProtocolMessageType('Acceleration', (_message.Message,), dict(
  DESCRIPTOR = _ACCELERATION,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Acceleration)
  ))
_sym_db.RegisterMessage(Acceleration)


# @@protoc_insertion_point(module_scope)