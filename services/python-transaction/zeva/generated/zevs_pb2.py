# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zevs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import generated.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='zevs.proto',
  package='zeva.transactions',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nzevs.proto\x12\x11zeva.transactions\x1a\x0c\x63ommon.proto\"(\n\x10ModelListRequest\x12\x14\n\x0corganization\x18\x01 \x01(\x04\"\x93\x01\n\x0cModelSummary\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04make\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04trim\x18\x05 \x01(\t\x12\r\n\x05range\x18\x06 \x01(\r\x12/\n\x07\x63redits\x18\x07 \x01(\x0b\x32\x1e.zeva.transactions.CreditValue\"\x93\x01\n\x0cModelDetails\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04make\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04trim\x18\x05 \x01(\t\x12\r\n\x05range\x18\x06 \x01(\r\x12/\n\x07\x63redits\x18\x07 \x01(\x0b\x32\x1e.zeva.transactions.CreditValue\"!\n\x13ModelDetailsRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"\\\n\x12ModelCreateRequest\x12\x0c\n\x04make\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04trim\x18\x05 \x01(\t\x12\r\n\x05range\x18\x06 \x01(\r\"!\n\x13ModelCreateResponse\x12\n\n\x02id\x18\x01 \x01(\x04\"h\n\x12ModelUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04make\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04trim\x18\x05 \x01(\t\x12\r\n\x05range\x18\x06 \x01(\r\"\x15\n\x13ModelUpdateResponse2\x87\x03\n\tZEVModels\x12T\n\nListModels\x12#.zeva.transactions.ModelListRequest\x1a\x1f.zeva.transactions.ModelSummary0\x01\x12Z\n\x0fGetModelDetails\x12&.zeva.transactions.ModelDetailsRequest\x1a\x1f.zeva.transactions.ModelDetails\x12\x63\n\x12\x43reateModelRequest\x12%.zeva.transactions.ModelCreateRequest\x1a&.zeva.transactions.ModelCreateResponse\x12\x63\n\x12UpdateModelRequest\x12%.zeva.transactions.ModelUpdateRequest\x1a&.zeva.transactions.ModelUpdateResponseb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_MODELLISTREQUEST = _descriptor.Descriptor(
  name='ModelListRequest',
  full_name='zeva.transactions.ModelListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='zeva.transactions.ModelListRequest.organization', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=47,
  serialized_end=87,
)


_MODELSUMMARY = _descriptor.Descriptor(
  name='ModelSummary',
  full_name='zeva.transactions.ModelSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='zeva.transactions.ModelSummary.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='make', full_name='zeva.transactions.ModelSummary.make', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='zeva.transactions.ModelSummary.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='zeva.transactions.ModelSummary.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trim', full_name='zeva.transactions.ModelSummary.trim', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='zeva.transactions.ModelSummary.range', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credits', full_name='zeva.transactions.ModelSummary.credits', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=90,
  serialized_end=237,
)


_MODELDETAILS = _descriptor.Descriptor(
  name='ModelDetails',
  full_name='zeva.transactions.ModelDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='zeva.transactions.ModelDetails.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='make', full_name='zeva.transactions.ModelDetails.make', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='zeva.transactions.ModelDetails.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='zeva.transactions.ModelDetails.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trim', full_name='zeva.transactions.ModelDetails.trim', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='zeva.transactions.ModelDetails.range', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credits', full_name='zeva.transactions.ModelDetails.credits', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=240,
  serialized_end=387,
)


_MODELDETAILSREQUEST = _descriptor.Descriptor(
  name='ModelDetailsRequest',
  full_name='zeva.transactions.ModelDetailsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='zeva.transactions.ModelDetailsRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=389,
  serialized_end=422,
)


_MODELCREATEREQUEST = _descriptor.Descriptor(
  name='ModelCreateRequest',
  full_name='zeva.transactions.ModelCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='make', full_name='zeva.transactions.ModelCreateRequest.make', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='zeva.transactions.ModelCreateRequest.model', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='zeva.transactions.ModelCreateRequest.type', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trim', full_name='zeva.transactions.ModelCreateRequest.trim', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='zeva.transactions.ModelCreateRequest.range', index=4,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=424,
  serialized_end=516,
)


_MODELCREATERESPONSE = _descriptor.Descriptor(
  name='ModelCreateResponse',
  full_name='zeva.transactions.ModelCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='zeva.transactions.ModelCreateResponse.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=518,
  serialized_end=551,
)


_MODELUPDATEREQUEST = _descriptor.Descriptor(
  name='ModelUpdateRequest',
  full_name='zeva.transactions.ModelUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='zeva.transactions.ModelUpdateRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='make', full_name='zeva.transactions.ModelUpdateRequest.make', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='zeva.transactions.ModelUpdateRequest.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='zeva.transactions.ModelUpdateRequest.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trim', full_name='zeva.transactions.ModelUpdateRequest.trim', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='zeva.transactions.ModelUpdateRequest.range', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=553,
  serialized_end=657,
)


_MODELUPDATERESPONSE = _descriptor.Descriptor(
  name='ModelUpdateResponse',
  full_name='zeva.transactions.ModelUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=659,
  serialized_end=680,
)

_MODELSUMMARY.fields_by_name['credits'].message_type = common__pb2._CREDITVALUE
_MODELDETAILS.fields_by_name['credits'].message_type = common__pb2._CREDITVALUE
DESCRIPTOR.message_types_by_name['ModelListRequest'] = _MODELLISTREQUEST
DESCRIPTOR.message_types_by_name['ModelSummary'] = _MODELSUMMARY
DESCRIPTOR.message_types_by_name['ModelDetails'] = _MODELDETAILS
DESCRIPTOR.message_types_by_name['ModelDetailsRequest'] = _MODELDETAILSREQUEST
DESCRIPTOR.message_types_by_name['ModelCreateRequest'] = _MODELCREATEREQUEST
DESCRIPTOR.message_types_by_name['ModelCreateResponse'] = _MODELCREATERESPONSE
DESCRIPTOR.message_types_by_name['ModelUpdateRequest'] = _MODELUPDATEREQUEST
DESCRIPTOR.message_types_by_name['ModelUpdateResponse'] = _MODELUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelListRequest = _reflection.GeneratedProtocolMessageType('ModelListRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODELLISTREQUEST,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelListRequest)
  })
_sym_db.RegisterMessage(ModelListRequest)

ModelSummary = _reflection.GeneratedProtocolMessageType('ModelSummary', (_message.Message,), {
  'DESCRIPTOR' : _MODELSUMMARY,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelSummary)
  })
_sym_db.RegisterMessage(ModelSummary)

ModelDetails = _reflection.GeneratedProtocolMessageType('ModelDetails', (_message.Message,), {
  'DESCRIPTOR' : _MODELDETAILS,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelDetails)
  })
_sym_db.RegisterMessage(ModelDetails)

ModelDetailsRequest = _reflection.GeneratedProtocolMessageType('ModelDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODELDETAILSREQUEST,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelDetailsRequest)
  })
_sym_db.RegisterMessage(ModelDetailsRequest)

ModelCreateRequest = _reflection.GeneratedProtocolMessageType('ModelCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODELCREATEREQUEST,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelCreateRequest)
  })
_sym_db.RegisterMessage(ModelCreateRequest)

ModelCreateResponse = _reflection.GeneratedProtocolMessageType('ModelCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODELCREATERESPONSE,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelCreateResponse)
  })
_sym_db.RegisterMessage(ModelCreateResponse)

ModelUpdateRequest = _reflection.GeneratedProtocolMessageType('ModelUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODELUPDATEREQUEST,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelUpdateRequest)
  })
_sym_db.RegisterMessage(ModelUpdateRequest)

ModelUpdateResponse = _reflection.GeneratedProtocolMessageType('ModelUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODELUPDATERESPONSE,
  '__module__' : 'zevs_pb2'
  # @@protoc_insertion_point(class_scope:zeva.transactions.ModelUpdateResponse)
  })
_sym_db.RegisterMessage(ModelUpdateResponse)



_ZEVMODELS = _descriptor.ServiceDescriptor(
  name='ZEVModels',
  full_name='zeva.transactions.ZEVModels',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=683,
  serialized_end=1074,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListModels',
    full_name='zeva.transactions.ZEVModels.ListModels',
    index=0,
    containing_service=None,
    input_type=_MODELLISTREQUEST,
    output_type=_MODELSUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetModelDetails',
    full_name='zeva.transactions.ZEVModels.GetModelDetails',
    index=1,
    containing_service=None,
    input_type=_MODELDETAILSREQUEST,
    output_type=_MODELDETAILS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateModelRequest',
    full_name='zeva.transactions.ZEVModels.CreateModelRequest',
    index=2,
    containing_service=None,
    input_type=_MODELCREATEREQUEST,
    output_type=_MODELCREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateModelRequest',
    full_name='zeva.transactions.ZEVModels.UpdateModelRequest',
    index=3,
    containing_service=None,
    input_type=_MODELUPDATEREQUEST,
    output_type=_MODELUPDATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ZEVMODELS)

DESCRIPTOR.services_by_name['ZEVModels'] = _ZEVMODELS

# @@protoc_insertion_point(module_scope)
