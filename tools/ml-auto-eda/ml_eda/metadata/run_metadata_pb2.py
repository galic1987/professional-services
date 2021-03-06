# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: run_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='run_metadata.proto',
  package='ml_eda.metadata',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12run_metadata.proto\x12\x0fml_eda.metadata\"\x89\x01\n\tAttribute\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.ml_eda.metadata.Attribute.Type\"3\n\x04Type\x12\r\n\tNUMERICAL\x10\x00\x12\x0f\n\x0b\x43\x41TEGORICAL\x10\x01\x12\x0b\n\x07TEXTUAL\x10\x02\"\xd3\x01\n\nDatasource\x12\n\n\x02id\x18\x01 \x01(\x03\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .ml_eda.metadata.Datasource.Type\x12\x10\n\x08location\x18\x03 \x01(\t\x12*\n\x06target\x18\x04 \x01(\x0b\x32\x1a.ml_eda.metadata.Attribute\x12,\n\x08\x66\x65\x61tures\x18\x05 \x03(\x0b\x32\x1a.ml_eda.metadata.Attribute\"\x1d\n\x04Type\x12\x07\n\x03\x43SV\x10\x00\x12\x0c\n\x08\x42IGQUERY\x10\x01\"\xd6\x02\n\x0cScalarMetric\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x30\n\x04name\x18\x02 \x02(\x0e\x32\".ml_eda.metadata.ScalarMetric.Name\x12\r\n\x05value\x18\x03 \x02(\x02\"\xf8\x01\n\x04Name\x12\x0f\n\x0b\x46_STATISTIC\x10\x01\x12\x0b\n\x07P_VALUE\x10\x02\x12\x14\n\x10INFORMATION_GAIN\x10\x03\x12\x1b\n\x17\x43ORRELATION_COEFFICIENT\x10\x04\x12\x08\n\x04MEAN\x10\x05\x12\n\n\x06MEDIAN\x10\x06\x12\x07\n\x03STD\x10\x07\x12\x07\n\x03MIN\x10\x08\x12\x07\n\x03MAX\x10\t\x12\x0f\n\x0bQUANTILE_25\x10\n\x12\x0f\n\x0bQUANTILE_75\x10\x0b\x12\x0f\n\x0bQUANTILE_95\x10\x0c\x12\x0c\n\x08SKEWNESS\x10\r\x12\x0f\n\x0b\x43\x41RDINALITY\x10\x0e\x12\x0f\n\x0bTOTAL_COUNT\x10\x0f\x12\x0b\n\x07MISSING\x10\x10\"I\n\x0fTableMetricCell\x12\x11\n\trow_index\x18\x01 \x01(\t\x12\x14\n\x0c\x63olumn_index\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x02(\x02\"T\n\x0eTableMetricRow\x12\x11\n\trow_index\x18\x01 \x02(\t\x12/\n\x05\x63\x65lls\x18\x02 \x03(\x0b\x32 .ml_eda.metadata.TableMetricCell\"\xe8\x01\n\x0bTableMetric\x12\n\n\x02id\x18\x01 \x01(\x03\x12/\n\x04name\x18\x02 \x01(\x0e\x32!.ml_eda.metadata.TableMetric.Name\x12\x16\n\x0e\x63olumn_indexes\x18\x03 \x03(\t\x12-\n\x04rows\x18\x04 \x03(\x0b\x32\x1f.ml_eda.metadata.TableMetricRow\"U\n\x04Name\x12\r\n\tHISTOGRAM\x10\x01\x12\x10\n\x0cVALUE_COUNTS\x10\x02\x12\x15\n\x11\x43ONTINGENCY_TABLE\x10\x03\x12\x15\n\x11TABLE_DESCRIPTIVE\x10\x04\"\x86\x03\n\x08\x41nalysis\x12\n\n\x02id\x18\x01 \x01(\x03\x12,\n\x04name\x18\x02 \x01(\x0e\x32\x1e.ml_eda.metadata.Analysis.Name\x12,\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\x1a.ml_eda.metadata.Attribute\x12/\n\x08smetrics\x18\x04 \x03(\x0b\x32\x1d.ml_eda.metadata.ScalarMetric\x12.\n\x08tmetrics\x18\x05 \x03(\x0b\x32\x1c.ml_eda.metadata.TableMetric\"\xb0\x01\n\x04Name\x12\x0f\n\x0b\x44\x45SCRIPTIVE\x10\x01\x12\r\n\tHISTOGRAM\x10\x02\x12\x10\n\x0cVALUE_COUNTS\x10\x03\x12\x15\n\x11\x43ONTINGENCY_TABLE\x10\x04\x12\x15\n\x11TABLE_DESCRIPTIVE\x10\x05\x12\x17\n\x13PEARSON_CORRELATION\x10\x06\x12\t\n\x05\x41NOVA\x10\x07\x12\x0e\n\nCHI_SQUARE\x10\x08\x12\x14\n\x10INFORMATION_GAIN\x10\t\"\x8e\x01\n\x0b\x41nalysisRun\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x15\n\rtimestamp_sec\x18\x02 \x01(\x01\x12/\n\ndatasource\x18\x03 \x01(\x0b\x32\x1b.ml_eda.metadata.Datasource\x12+\n\x08\x61nalyses\x18\x04 \x03(\x0b\x32\x19.ml_eda.metadata.Analysis')
)



_ATTRIBUTE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ml_eda.metadata.Attribute.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NUMERICAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORICAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXTUAL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=126,
  serialized_end=177,
)
_sym_db.RegisterEnumDescriptor(_ATTRIBUTE_TYPE)

_DATASOURCE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ml_eda.metadata.Datasource.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CSV', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIGQUERY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=362,
  serialized_end=391,
)
_sym_db.RegisterEnumDescriptor(_DATASOURCE_TYPE)

_SCALARMETRIC_NAME = _descriptor.EnumDescriptor(
  name='Name',
  full_name='ml_eda.metadata.ScalarMetric.Name',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='F_STATISTIC', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P_VALUE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFORMATION_GAIN', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CORRELATION_COEFFICIENT', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEAN', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIAN', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STD', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANTILE_25', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANTILE_75', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANTILE_95', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKEWNESS', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARDINALITY', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_COUNT', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING', index=15, number=16,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=488,
  serialized_end=736,
)
_sym_db.RegisterEnumDescriptor(_SCALARMETRIC_NAME)

_TABLEMETRIC_NAME = _descriptor.EnumDescriptor(
  name='Name',
  full_name='ml_eda.metadata.TableMetric.Name',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HISTOGRAM', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_COUNTS', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINGENCY_TABLE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TABLE_DESCRIPTIVE', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1047,
  serialized_end=1132,
)
_sym_db.RegisterEnumDescriptor(_TABLEMETRIC_NAME)

_ANALYSIS_NAME = _descriptor.EnumDescriptor(
  name='Name',
  full_name='ml_eda.metadata.Analysis.Name',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTIVE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HISTOGRAM', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_COUNTS', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINGENCY_TABLE', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TABLE_DESCRIPTIVE', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEARSON_CORRELATION', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANOVA', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHI_SQUARE', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFORMATION_GAIN', index=8, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1349,
  serialized_end=1525,
)
_sym_db.RegisterEnumDescriptor(_ANALYSIS_NAME)


_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='ml_eda.metadata.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.Attribute.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ml_eda.metadata.Attribute.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ml_eda.metadata.Attribute.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTRIBUTE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=177,
)


_DATASOURCE = _descriptor.Descriptor(
  name='Datasource',
  full_name='ml_eda.metadata.Datasource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.Datasource.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ml_eda.metadata.Datasource.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='ml_eda.metadata.Datasource.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='ml_eda.metadata.Datasource.target', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='ml_eda.metadata.Datasource.features', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATASOURCE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=391,
)


_SCALARMETRIC = _descriptor.Descriptor(
  name='ScalarMetric',
  full_name='ml_eda.metadata.ScalarMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.ScalarMetric.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ml_eda.metadata.ScalarMetric.name', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ml_eda.metadata.ScalarMetric.value', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCALARMETRIC_NAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=736,
)


_TABLEMETRICCELL = _descriptor.Descriptor(
  name='TableMetricCell',
  full_name='ml_eda.metadata.TableMetricCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_index', full_name='ml_eda.metadata.TableMetricCell.row_index', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_index', full_name='ml_eda.metadata.TableMetricCell.column_index', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ml_eda.metadata.TableMetricCell.value', index=2,
      number=3, type=2, cpp_type=6, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=738,
  serialized_end=811,
)


_TABLEMETRICROW = _descriptor.Descriptor(
  name='TableMetricRow',
  full_name='ml_eda.metadata.TableMetricRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_index', full_name='ml_eda.metadata.TableMetricRow.row_index', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cells', full_name='ml_eda.metadata.TableMetricRow.cells', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=813,
  serialized_end=897,
)


_TABLEMETRIC = _descriptor.Descriptor(
  name='TableMetric',
  full_name='ml_eda.metadata.TableMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.TableMetric.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ml_eda.metadata.TableMetric.name', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_indexes', full_name='ml_eda.metadata.TableMetric.column_indexes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='ml_eda.metadata.TableMetric.rows', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TABLEMETRIC_NAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=900,
  serialized_end=1132,
)


_ANALYSIS = _descriptor.Descriptor(
  name='Analysis',
  full_name='ml_eda.metadata.Analysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.Analysis.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ml_eda.metadata.Analysis.name', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='ml_eda.metadata.Analysis.features', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='smetrics', full_name='ml_eda.metadata.Analysis.smetrics', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tmetrics', full_name='ml_eda.metadata.Analysis.tmetrics', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANALYSIS_NAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1135,
  serialized_end=1525,
)


_ANALYSISRUN = _descriptor.Descriptor(
  name='AnalysisRun',
  full_name='ml_eda.metadata.AnalysisRun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ml_eda.metadata.AnalysisRun.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_sec', full_name='ml_eda.metadata.AnalysisRun.timestamp_sec', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datasource', full_name='ml_eda.metadata.AnalysisRun.datasource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analyses', full_name='ml_eda.metadata.AnalysisRun.analyses', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1528,
  serialized_end=1670,
)

_ATTRIBUTE.fields_by_name['type'].enum_type = _ATTRIBUTE_TYPE
_ATTRIBUTE_TYPE.containing_type = _ATTRIBUTE
_DATASOURCE.fields_by_name['type'].enum_type = _DATASOURCE_TYPE
_DATASOURCE.fields_by_name['target'].message_type = _ATTRIBUTE
_DATASOURCE.fields_by_name['features'].message_type = _ATTRIBUTE
_DATASOURCE_TYPE.containing_type = _DATASOURCE
_SCALARMETRIC.fields_by_name['name'].enum_type = _SCALARMETRIC_NAME
_SCALARMETRIC_NAME.containing_type = _SCALARMETRIC
_TABLEMETRICROW.fields_by_name['cells'].message_type = _TABLEMETRICCELL
_TABLEMETRIC.fields_by_name['name'].enum_type = _TABLEMETRIC_NAME
_TABLEMETRIC.fields_by_name['rows'].message_type = _TABLEMETRICROW
_TABLEMETRIC_NAME.containing_type = _TABLEMETRIC
_ANALYSIS.fields_by_name['name'].enum_type = _ANALYSIS_NAME
_ANALYSIS.fields_by_name['features'].message_type = _ATTRIBUTE
_ANALYSIS.fields_by_name['smetrics'].message_type = _SCALARMETRIC
_ANALYSIS.fields_by_name['tmetrics'].message_type = _TABLEMETRIC
_ANALYSIS_NAME.containing_type = _ANALYSIS
_ANALYSISRUN.fields_by_name['datasource'].message_type = _DATASOURCE
_ANALYSISRUN.fields_by_name['analyses'].message_type = _ANALYSIS
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['Datasource'] = _DATASOURCE
DESCRIPTOR.message_types_by_name['ScalarMetric'] = _SCALARMETRIC
DESCRIPTOR.message_types_by_name['TableMetricCell'] = _TABLEMETRICCELL
DESCRIPTOR.message_types_by_name['TableMetricRow'] = _TABLEMETRICROW
DESCRIPTOR.message_types_by_name['TableMetric'] = _TABLEMETRIC
DESCRIPTOR.message_types_by_name['Analysis'] = _ANALYSIS
DESCRIPTOR.message_types_by_name['AnalysisRun'] = _ANALYSISRUN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
  'DESCRIPTOR' : _ATTRIBUTE,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.Attribute)
  })
_sym_db.RegisterMessage(Attribute)

Datasource = _reflection.GeneratedProtocolMessageType('Datasource', (_message.Message,), {
  'DESCRIPTOR' : _DATASOURCE,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.Datasource)
  })
_sym_db.RegisterMessage(Datasource)

ScalarMetric = _reflection.GeneratedProtocolMessageType('ScalarMetric', (_message.Message,), {
  'DESCRIPTOR' : _SCALARMETRIC,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.ScalarMetric)
  })
_sym_db.RegisterMessage(ScalarMetric)

TableMetricCell = _reflection.GeneratedProtocolMessageType('TableMetricCell', (_message.Message,), {
  'DESCRIPTOR' : _TABLEMETRICCELL,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.TableMetricCell)
  })
_sym_db.RegisterMessage(TableMetricCell)

TableMetricRow = _reflection.GeneratedProtocolMessageType('TableMetricRow', (_message.Message,), {
  'DESCRIPTOR' : _TABLEMETRICROW,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.TableMetricRow)
  })
_sym_db.RegisterMessage(TableMetricRow)

TableMetric = _reflection.GeneratedProtocolMessageType('TableMetric', (_message.Message,), {
  'DESCRIPTOR' : _TABLEMETRIC,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.TableMetric)
  })
_sym_db.RegisterMessage(TableMetric)

Analysis = _reflection.GeneratedProtocolMessageType('Analysis', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSIS,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.Analysis)
  })
_sym_db.RegisterMessage(Analysis)

AnalysisRun = _reflection.GeneratedProtocolMessageType('AnalysisRun', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSISRUN,
  '__module__' : 'run_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ml_eda.metadata.AnalysisRun)
  })
_sym_db.RegisterMessage(AnalysisRun)


# @@protoc_insertion_point(module_scope)
