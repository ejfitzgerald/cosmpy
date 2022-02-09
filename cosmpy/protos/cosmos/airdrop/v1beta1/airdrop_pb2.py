# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/airdrop/v1beta1/airdrop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/airdrop/v1beta1/airdrop.proto',
  package='cosmos.airdrop.v1beta1',
  syntax='proto3',
  serialized_options=b'Z,github.com/cosmos/cosmos-sdk/x/airdrop/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$cosmos/airdrop/v1beta1/airdrop.proto\x12\x16\x63osmos.airdrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xa5\x01\n\x04\x46und\x12<\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x11\xf2\xde\x1f\ryaml:\"amount\"\x12Y\n\x0b\x64rip_amount\x18\x02 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:\"drip_amount\":\x04\xe8\xa0\x1f\x01\"x\n\nActiveFund\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12G\n\x04\x66und\x18\x02 \x01(\x0b\x32\x1c.cosmos.airdrop.v1beta1.FundB\x1b\xf2\xde\x1f\x17yaml:\"blocks_remaining\"\"3\n\x06Params\x12)\n\nallow_list\x18\x01 \x03(\tB\x15\xf2\xde\x1f\x11yaml:\"allow_list\"B.Z,github.com/cosmos/cosmos-sdk/x/airdrop/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_FUND = _descriptor.Descriptor(
  name='Fund',
  full_name='cosmos.airdrop.v1beta1.Fund',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.airdrop.v1beta1.Fund.amount', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\ryaml:\"amount\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drip_amount', full_name='cosmos.airdrop.v1beta1.Fund.drip_amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000\362\336\037\022yaml:\"drip_amount\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=311,
)


_ACTIVEFUND = _descriptor.Descriptor(
  name='ActiveFund',
  full_name='cosmos.airdrop.v1beta1.ActiveFund',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='cosmos.airdrop.v1beta1.ActiveFund.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\ryaml:\"sender\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fund', full_name='cosmos.airdrop.v1beta1.ActiveFund.fund', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"blocks_remaining\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=313,
  serialized_end=433,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.airdrop.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_list', full_name='cosmos.airdrop.v1beta1.Params.allow_list', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"allow_list\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=435,
  serialized_end=486,
)

_FUND.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_ACTIVEFUND.fields_by_name['fund'].message_type = _FUND
DESCRIPTOR.message_types_by_name['Fund'] = _FUND
DESCRIPTOR.message_types_by_name['ActiveFund'] = _ACTIVEFUND
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fund = _reflection.GeneratedProtocolMessageType('Fund', (_message.Message,), {
  'DESCRIPTOR' : _FUND,
  '__module__' : 'cosmos.airdrop.v1beta1.airdrop_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.airdrop.v1beta1.Fund)
  })
_sym_db.RegisterMessage(Fund)

ActiveFund = _reflection.GeneratedProtocolMessageType('ActiveFund', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVEFUND,
  '__module__' : 'cosmos.airdrop.v1beta1.airdrop_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.airdrop.v1beta1.ActiveFund)
  })
_sym_db.RegisterMessage(ActiveFund)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.airdrop.v1beta1.airdrop_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.airdrop.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_FUND.fields_by_name['amount']._options = None
_FUND.fields_by_name['drip_amount']._options = None
_FUND._options = None
_ACTIVEFUND.fields_by_name['sender']._options = None
_ACTIVEFUND.fields_by_name['fund']._options = None
_PARAMS.fields_by_name['allow_list']._options = None
# @@protoc_insertion_point(module_scope)