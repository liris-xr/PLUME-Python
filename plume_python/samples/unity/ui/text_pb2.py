# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/ui/text.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2
from common import color_pb2 as common_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13unity/ui/text.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x12\x63ommon/color.proto\"A\n\nTextCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"B\n\x0bTextDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"\xa3\x07\n\nTextUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x39\n\x07\x66ont_id\x18\x03 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01\x88\x01\x01\x12\x36\n\nfont_style\x18\x04 \x01(\x0e\x32\x1d.plume.sample.unity.FontStyleH\x02\x88\x01\x01\x12\x16\n\tfont_size\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12.\n\x05\x63olor\x18\x06 \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x04\x88\x01\x01\x12\x19\n\x0cline_spacing\x18\x07 \x01(\x02H\x05\x88\x01\x01\x12\x1e\n\x11support_rich_text\x18\x08 \x01(\x08H\x06\x88\x01\x01\x12\x36\n\talignment\x18\t \x01(\x0e\x32\x1e.plume.sample.unity.TextAnchorH\x07\x88\x01\x01\x12\x1e\n\x11\x61lign_by_geometry\x18\n \x01(\x08H\x08\x88\x01\x01\x12H\n\x13horizontal_overflow\x18\x0b \x01(\x0e\x32&.plume.sample.unity.HorizontalWrapModeH\t\x88\x01\x01\x12\x44\n\x11vertical_overflow\x18\x0c \x01(\x0e\x32$.plume.sample.unity.VerticalWrapModeH\n\x88\x01\x01\x12%\n\x18resize_text_for_best_fit\x18\r \x01(\x08H\x0b\x88\x01\x01\x12!\n\x14resize_text_min_size\x18\x0e \x01(\x05H\x0c\x88\x01\x01\x12!\n\x14resize_text_max_size\x18\x0f \x01(\x05H\r\x88\x01\x01\x42\x07\n\x05_textB\n\n\x08_font_idB\r\n\x0b_font_styleB\x0c\n\n_font_sizeB\x08\n\x06_colorB\x0f\n\r_line_spacingB\x14\n\x12_support_rich_textB\x0c\n\n_alignmentB\x14\n\x12_align_by_geometryB\x16\n\x14_horizontal_overflowB\x14\n\x12_vertical_overflowB\x1b\n\x19_resize_text_for_best_fitB\x17\n\x15_resize_text_min_sizeB\x17\n\x15_resize_text_max_size*V\n\x12HorizontalWrapMode\x12\x1d\n\x19HORIZONTAL_WRAP_MODE_WRAP\x10\x00\x12!\n\x1dHORIZONTAL_WRAP_MODE_OVERFLOW\x10\x01*T\n\x10VerticalWrapMode\x12\x1f\n\x1bVERTICAL_WRAP_MODE_TRUNCATE\x10\x00\x12\x1f\n\x1bVERTICAL_WRAP_MODE_OVERFLOW\x10\x01*\x94\x02\n\nTextAnchor\x12\x1a\n\x16TEXT_ANCHOR_UPPER_LEFT\x10\x00\x12\x1c\n\x18TEXT_ANCHOR_UPPER_CENTER\x10\x01\x12\x1b\n\x17TEXT_ANCHOR_UPPER_RIGHT\x10\x02\x12\x1b\n\x17TEXT_ANCHOR_MIDDLE_LEFT\x10\x03\x12\x1d\n\x19TEXT_ANCHOR_MIDDLE_CENTER\x10\x04\x12\x1c\n\x18TEXT_ANCHOR_MIDDLE_RIGHT\x10\x05\x12\x1a\n\x16TEXT_ANCHOR_LOWER_LEFT\x10\x06\x12\x1c\n\x18TEXT_ANCHOR_LOWER_CENTER\x10\x07\x12\x1b\n\x17TEXT_ANCHOR_LOWER_RIGHT\x10\x08*n\n\tFontStyle\x12\x15\n\x11\x46ONT_STYLE_NORMAL\x10\x00\x12\x13\n\x0f\x46ONT_STYLE_BOLD\x10\x01\x12\x15\n\x11\x46ONT_STYLE_ITALIC\x10\x02\x12\x1e\n\x1a\x46ONT_STYLE_BOLD_AND_ITALIC\x10\x03\x42\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.ui.text_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\025PLUME.Sample.Unity.UI'
  _globals['_HORIZONTALWRAPMODE']._serialized_start=1157
  _globals['_HORIZONTALWRAPMODE']._serialized_end=1243
  _globals['_VERTICALWRAPMODE']._serialized_start=1245
  _globals['_VERTICALWRAPMODE']._serialized_end=1329
  _globals['_TEXTANCHOR']._serialized_start=1332
  _globals['_TEXTANCHOR']._serialized_end=1608
  _globals['_FONTSTYLE']._serialized_start=1610
  _globals['_FONTSTYLE']._serialized_end=1720
  _globals['_TEXTCREATE']._serialized_start=88
  _globals['_TEXTCREATE']._serialized_end=153
  _globals['_TEXTDESTROY']._serialized_start=155
  _globals['_TEXTDESTROY']._serialized_end=221
  _globals['_TEXTUPDATE']._serialized_start=224
  _globals['_TEXTUPDATE']._serialized_end=1155
# @@protoc_insertion_point(module_scope)