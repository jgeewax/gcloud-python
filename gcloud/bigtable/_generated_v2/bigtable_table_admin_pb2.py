# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/admin/v2/bigtable_table_admin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from gcloud.bigtable._generated_v2 import table_pb2 as google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/admin/v2/bigtable_table_admin.proto',
  package='google.bigtable.admin.v2',
  syntax='proto3',
  serialized_pb=_b('\n3google/bigtable/admin/v2/bigtable_table_admin.proto\x12\x18google.bigtable.admin.v2\x1a\x1cgoogle/api/annotations.proto\x1a$google/bigtable/admin/v2/table.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xc6\x01\n\x12\x43reateTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\t\x12.\n\x05table\x18\x03 \x01(\x0b\x32\x1f.google.bigtable.admin.v2.Table\x12J\n\x0einitial_splits\x18\x04 \x03(\x0b\x32\x32.google.bigtable.admin.v2.CreateTableRequest.Split\x1a\x14\n\x05Split\x12\x0b\n\x03key\x18\x01 \x01(\x0c\"m\n\x13\x44ropRowRangeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0erow_key_prefix\x18\x02 \x01(\x0cH\x00\x12$\n\x1a\x64\x65lete_all_data_from_table\x18\x03 \x01(\x08H\x00\x42\x08\n\x06target\"i\n\x11ListTablesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x04view\x18\x02 \x01(\x0e\x32$.google.bigtable.admin.v2.Table.View\x12\x12\n\npage_token\x18\x03 \x01(\t\"^\n\x12ListTablesResponse\x12/\n\x06tables\x18\x01 \x03(\x0b\x32\x1f.google.bigtable.admin.v2.Table\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"S\n\x0fGetTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x04view\x18\x02 \x01(\x0e\x32$.google.bigtable.admin.v2.Table.View\"\"\n\x12\x44\x65leteTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xae\x02\n\x1bModifyColumnFamiliesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12Y\n\rmodifications\x18\x02 \x03(\x0b\x32\x42.google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification\x1a\xa5\x01\n\x0cModification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x38\n\x06\x63reate\x18\x02 \x01(\x0b\x32&.google.bigtable.admin.v2.ColumnFamilyH\x00\x12\x38\n\x06update\x18\x03 \x01(\x0b\x32&.google.bigtable.admin.v2.ColumnFamilyH\x00\x12\x0e\n\x04\x64rop\x18\x04 \x01(\x08H\x00\x42\x05\n\x03mod2\xb4\x07\n\x12\x42igtableTableAdmin\x12\x91\x01\n\x0b\x43reateTable\x12,.google.bigtable.admin.v2.CreateTableRequest\x1a\x1f.google.bigtable.admin.v2.Table\"3\x82\xd3\xe4\x93\x02-\"(/v2/{name=projects/*/instances/*}/tables:\x01*\x12\x99\x01\n\nListTables\x12+.google.bigtable.admin.v2.ListTablesRequest\x1a,.google.bigtable.admin.v2.ListTablesResponse\"0\x82\xd3\xe4\x93\x02*\x12(/v2/{name=projects/*/instances/*}/tables\x12\x8a\x01\n\x08GetTable\x12).google.bigtable.admin.v2.GetTableRequest\x1a\x1f.google.bigtable.admin.v2.Table\"2\x82\xd3\xe4\x93\x02,\x12*/v2/{name=projects/*/instances/*/tables/*}\x12\x87\x01\n\x0b\x44\x65leteTable\x12,.google.bigtable.admin.v2.DeleteTableRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,**/v2/{name=projects/*/instances/*/tables/*}\x12\xba\x01\n\x14ModifyColumnFamilies\x12\x35.google.bigtable.admin.v2.ModifyColumnFamiliesRequest\x1a\x1f.google.bigtable.admin.v2.Table\"J\x82\xd3\xe4\x93\x02\x44\"?/v2/{name=projects/*/instances/*/tables/*}:modifyColumnFamilies:\x01*\x12\x99\x01\n\x0c\x44ropRowRange\x12-.google.bigtable.admin.v2.DropRowRangeRequest\x1a\x16.google.protobuf.Empty\"B\x82\xd3\xe4\x93\x02<\"7/v2/{name=projects/*/instances/*/tables/*}:dropRowRange:\x01*B9\n\x1c\x63om.google.bigtable.admin.v2B\x17\x42igtableTableAdminProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREATETABLEREQUEST_SPLIT = _descriptor.Descriptor(
  name='Split',
  full_name='google.bigtable.admin.v2.CreateTableRequest.Split',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.bigtable.admin.v2.CreateTableRequest.Split.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=357,
  serialized_end=377,
)

_CREATETABLEREQUEST = _descriptor.Descriptor(
  name='CreateTableRequest',
  full_name='google.bigtable.admin.v2.CreateTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.CreateTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='google.bigtable.admin.v2.CreateTableRequest.table_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='google.bigtable.admin.v2.CreateTableRequest.table', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_splits', full_name='google.bigtable.admin.v2.CreateTableRequest.initial_splits', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CREATETABLEREQUEST_SPLIT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=377,
)


_DROPROWRANGEREQUEST = _descriptor.Descriptor(
  name='DropRowRangeRequest',
  full_name='google.bigtable.admin.v2.DropRowRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.DropRowRangeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row_key_prefix', full_name='google.bigtable.admin.v2.DropRowRangeRequest.row_key_prefix', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_all_data_from_table', full_name='google.bigtable.admin.v2.DropRowRangeRequest.delete_all_data_from_table', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='target', full_name='google.bigtable.admin.v2.DropRowRangeRequest.target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=379,
  serialized_end=488,
)


_LISTTABLESREQUEST = _descriptor.Descriptor(
  name='ListTablesRequest',
  full_name='google.bigtable.admin.v2.ListTablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.ListTablesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.bigtable.admin.v2.ListTablesRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.bigtable.admin.v2.ListTablesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=490,
  serialized_end=595,
)


_LISTTABLESRESPONSE = _descriptor.Descriptor(
  name='ListTablesResponse',
  full_name='google.bigtable.admin.v2.ListTablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tables', full_name='google.bigtable.admin.v2.ListTablesResponse.tables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.bigtable.admin.v2.ListTablesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=597,
  serialized_end=691,
)


_GETTABLEREQUEST = _descriptor.Descriptor(
  name='GetTableRequest',
  full_name='google.bigtable.admin.v2.GetTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.GetTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.bigtable.admin.v2.GetTableRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=693,
  serialized_end=776,
)


_DELETETABLEREQUEST = _descriptor.Descriptor(
  name='DeleteTableRequest',
  full_name='google.bigtable.admin.v2.DeleteTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.DeleteTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=778,
  serialized_end=812,
)


_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION = _descriptor.Descriptor(
  name='Modification',
  full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification.create', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification.update', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification.drop', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='mod', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification.mod',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=952,
  serialized_end=1117,
)

_MODIFYCOLUMNFAMILIESREQUEST = _descriptor.Descriptor(
  name='ModifyColumnFamiliesRequest',
  full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modifications', full_name='google.bigtable.admin.v2.ModifyColumnFamiliesRequest.modifications', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=1117,
)

_CREATETABLEREQUEST_SPLIT.containing_type = _CREATETABLEREQUEST
_CREATETABLEREQUEST.fields_by_name['table'].message_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._TABLE
_CREATETABLEREQUEST.fields_by_name['initial_splits'].message_type = _CREATETABLEREQUEST_SPLIT
_DROPROWRANGEREQUEST.oneofs_by_name['target'].fields.append(
  _DROPROWRANGEREQUEST.fields_by_name['row_key_prefix'])
_DROPROWRANGEREQUEST.fields_by_name['row_key_prefix'].containing_oneof = _DROPROWRANGEREQUEST.oneofs_by_name['target']
_DROPROWRANGEREQUEST.oneofs_by_name['target'].fields.append(
  _DROPROWRANGEREQUEST.fields_by_name['delete_all_data_from_table'])
_DROPROWRANGEREQUEST.fields_by_name['delete_all_data_from_table'].containing_oneof = _DROPROWRANGEREQUEST.oneofs_by_name['target']
_LISTTABLESREQUEST.fields_by_name['view'].enum_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._TABLE_VIEW
_LISTTABLESRESPONSE.fields_by_name['tables'].message_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._TABLE
_GETTABLEREQUEST.fields_by_name['view'].enum_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._TABLE_VIEW
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['create'].message_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._COLUMNFAMILY
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['update'].message_type = google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2._COLUMNFAMILY
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.containing_type = _MODIFYCOLUMNFAMILIESREQUEST
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod'].fields.append(
  _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['create'])
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['create'].containing_oneof = _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod']
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod'].fields.append(
  _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['update'])
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['update'].containing_oneof = _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod']
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod'].fields.append(
  _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['drop'])
_MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.fields_by_name['drop'].containing_oneof = _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION.oneofs_by_name['mod']
_MODIFYCOLUMNFAMILIESREQUEST.fields_by_name['modifications'].message_type = _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION
DESCRIPTOR.message_types_by_name['CreateTableRequest'] = _CREATETABLEREQUEST
DESCRIPTOR.message_types_by_name['DropRowRangeRequest'] = _DROPROWRANGEREQUEST
DESCRIPTOR.message_types_by_name['ListTablesRequest'] = _LISTTABLESREQUEST
DESCRIPTOR.message_types_by_name['ListTablesResponse'] = _LISTTABLESRESPONSE
DESCRIPTOR.message_types_by_name['GetTableRequest'] = _GETTABLEREQUEST
DESCRIPTOR.message_types_by_name['DeleteTableRequest'] = _DELETETABLEREQUEST
DESCRIPTOR.message_types_by_name['ModifyColumnFamiliesRequest'] = _MODIFYCOLUMNFAMILIESREQUEST

CreateTableRequest = _reflection.GeneratedProtocolMessageType('CreateTableRequest', (_message.Message,), dict(

  Split = _reflection.GeneratedProtocolMessageType('Split', (_message.Message,), dict(
    DESCRIPTOR = _CREATETABLEREQUEST_SPLIT,
    __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.CreateTableRequest.Split)
    ))
  ,
  DESCRIPTOR = _CREATETABLEREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.CreateTableRequest)
  ))
_sym_db.RegisterMessage(CreateTableRequest)
_sym_db.RegisterMessage(CreateTableRequest.Split)

DropRowRangeRequest = _reflection.GeneratedProtocolMessageType('DropRowRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _DROPROWRANGEREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.DropRowRangeRequest)
  ))
_sym_db.RegisterMessage(DropRowRangeRequest)

ListTablesRequest = _reflection.GeneratedProtocolMessageType('ListTablesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTABLESREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.ListTablesRequest)
  ))
_sym_db.RegisterMessage(ListTablesRequest)

ListTablesResponse = _reflection.GeneratedProtocolMessageType('ListTablesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTABLESRESPONSE,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.ListTablesResponse)
  ))
_sym_db.RegisterMessage(ListTablesResponse)

GetTableRequest = _reflection.GeneratedProtocolMessageType('GetTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTABLEREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.GetTableRequest)
  ))
_sym_db.RegisterMessage(GetTableRequest)

DeleteTableRequest = _reflection.GeneratedProtocolMessageType('DeleteTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETETABLEREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.DeleteTableRequest)
  ))
_sym_db.RegisterMessage(DeleteTableRequest)

ModifyColumnFamiliesRequest = _reflection.GeneratedProtocolMessageType('ModifyColumnFamiliesRequest', (_message.Message,), dict(

  Modification = _reflection.GeneratedProtocolMessageType('Modification', (_message.Message,), dict(
    DESCRIPTOR = _MODIFYCOLUMNFAMILIESREQUEST_MODIFICATION,
    __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
    # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification)
    ))
  ,
  DESCRIPTOR = _MODIFYCOLUMNFAMILIESREQUEST,
  __module__ = 'google.bigtable.admin.v2.bigtable_table_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.ModifyColumnFamiliesRequest)
  ))
_sym_db.RegisterMessage(ModifyColumnFamiliesRequest)
_sym_db.RegisterMessage(ModifyColumnFamiliesRequest.Modification)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.google.bigtable.admin.v2B\027BigtableTableAdminProtoP\001'))
import abc
import six
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBigtableTableAdminServicer(object):
  """<fill me in later!>"""
  def CreateTable(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def ListTables(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetTable(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def DeleteTable(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def ModifyColumnFamilies(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def DropRowRange(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

class BetaBigtableTableAdminStub(object):
  """The interface to which stubs will conform."""
  def CreateTable(self, request, timeout):
    raise NotImplementedError()
  CreateTable.future = None
  def ListTables(self, request, timeout):
    raise NotImplementedError()
  ListTables.future = None
  def GetTable(self, request, timeout):
    raise NotImplementedError()
  GetTable.future = None
  def DeleteTable(self, request, timeout):
    raise NotImplementedError()
  DeleteTable.future = None
  def ModifyColumnFamilies(self, request, timeout):
    raise NotImplementedError()
  ModifyColumnFamilies.future = None
  def DropRowRange(self, request, timeout):
    raise NotImplementedError()
  DropRowRange.future = None

def beta_create_BigtableTableAdmin_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.protobuf.empty_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.protobuf.empty_pb2
  request_deserializers = {
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'CreateTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableRequest.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DeleteTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteTableRequest.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DropRowRange'): google.bigtable.admin.v2.bigtable_table_admin_pb2.DropRowRangeRequest.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'GetTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.GetTableRequest.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ListTables'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesRequest.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ModifyColumnFamilies'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ModifyColumnFamiliesRequest.FromString,
  }
  response_serializers = {
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'CreateTable'): google.bigtable.admin.v2.table_pb2.Table.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DeleteTable'): google.protobuf.empty_pb2.Empty.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DropRowRange'): google.protobuf.empty_pb2.Empty.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'GetTable'): google.bigtable.admin.v2.table_pb2.Table.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ListTables'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesResponse.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ModifyColumnFamilies'): google.bigtable.admin.v2.table_pb2.Table.SerializeToString,
  }
  method_implementations = {
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'CreateTable'): face_utilities.unary_unary_inline(servicer.CreateTable),
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DeleteTable'): face_utilities.unary_unary_inline(servicer.DeleteTable),
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DropRowRange'): face_utilities.unary_unary_inline(servicer.DropRowRange),
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'GetTable'): face_utilities.unary_unary_inline(servicer.GetTable),
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ListTables'): face_utilities.unary_unary_inline(servicer.ListTables),
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ModifyColumnFamilies'): face_utilities.unary_unary_inline(servicer.ModifyColumnFamilies),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BigtableTableAdmin_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.protobuf.empty_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.bigtable.admin.v2.table_pb2
  import google.bigtable.admin.v2.bigtable_table_admin_pb2
  import google.protobuf.empty_pb2
  request_serializers = {
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'CreateTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableRequest.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DeleteTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteTableRequest.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DropRowRange'): google.bigtable.admin.v2.bigtable_table_admin_pb2.DropRowRangeRequest.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'GetTable'): google.bigtable.admin.v2.bigtable_table_admin_pb2.GetTableRequest.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ListTables'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesRequest.SerializeToString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ModifyColumnFamilies'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ModifyColumnFamiliesRequest.SerializeToString,
  }
  response_deserializers = {
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'CreateTable'): google.bigtable.admin.v2.table_pb2.Table.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DeleteTable'): google.protobuf.empty_pb2.Empty.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'DropRowRange'): google.protobuf.empty_pb2.Empty.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'GetTable'): google.bigtable.admin.v2.table_pb2.Table.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ListTables'): google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesResponse.FromString,
    ('google.bigtable.admin.v2.BigtableTableAdmin', 'ModifyColumnFamilies'): google.bigtable.admin.v2.table_pb2.Table.FromString,
  }
  cardinalities = {
    'CreateTable': cardinality.Cardinality.UNARY_UNARY,
    'DeleteTable': cardinality.Cardinality.UNARY_UNARY,
    'DropRowRange': cardinality.Cardinality.UNARY_UNARY,
    'GetTable': cardinality.Cardinality.UNARY_UNARY,
    'ListTables': cardinality.Cardinality.UNARY_UNARY,
    'ModifyColumnFamilies': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'google.bigtable.admin.v2.BigtableTableAdmin', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
