# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/proto/pythonServicer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from message.proto import APMFactory_pb2 as message_dot_proto_dot_APMFactory__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"message/proto/pythonServicer.proto\x12\tprotoData\x1a\x1emessage/proto/APMFactory.proto\"L\n\x13MainServicerRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\x04\x12!\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x13.protoData.NodeData\"V\n\x1aSubordinateServicerRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\x04\x12\x11\n\tdata_type\x18\x02 \x01(\x04\x12\x11\n\trqst_data\x18\x03 \x01(\x0c\"7\n\x0fServiceResponse\x12\x12\n\nmessage_id\x18\x01 \x01(\x04\x12\x10\n\x08res_data\x18\x02 \x01(\x0c\"(\n\rRequestPrompt\x12\x17\n\x0fprompt_sentence\x18\x01 \x01(\t\"\x1b\n\x0bRequestList\x12\x0c\n\x04list\x18\x01 \x03(\t\"-\n\x08WordList\x12!\n\x05words\x18\x01 \x03(\x0b\x32\x12.protoData.WordVec\"7\n\x07WordVec\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x11\n\tdimension\x18\x02 \x01(\x05\x12\x0b\n\x03vec\x18\x03 \x03(\x02\"?\n\x0bSentenceVec\x12\x10\n\x08sentence\x18\x01 \x01(\t\x12\x11\n\tdimension\x18\x02 \x01(\x05\x12\x0b\n\x03vec\x18\x03 \x03(\x02\x32\xbe\x01\n\nAPMService\x12P\n\x12MainServiceRequest\x12\x1e.protoData.MainServicerRequest\x1a\x1a.protoData.ServiceResponse\x12^\n\x19SubordinateServiceRequest\x12%.protoData.SubordinateServicerRequest\x1a\x1a.protoData.ServiceResponse2\xa2\x02\n\x14SubFunctionalService\x12\x44\n\x13\x45mbeddingNounChunks\x12\x18.protoData.RequestPrompt\x1a\x13.protoData.WordList\x12\x45\n\x11\x45mbeddingSentence\x12\x18.protoData.RequestPrompt\x1a\x16.protoData.SentenceVec\x12<\n\rEmbeddingList\x12\x16.protoData.RequestList\x1a\x13.protoData.WordList\x12?\n\x0e\x45mbeddingTopic\x12\x18.protoData.RequestPrompt\x1a\x13.protoData.WordListB\x17Z\x15golang-client/messageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message.proto.pythonServicer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025golang-client/message'
  _globals['_MAINSERVICERREQUEST']._serialized_start=81
  _globals['_MAINSERVICERREQUEST']._serialized_end=157
  _globals['_SUBORDINATESERVICERREQUEST']._serialized_start=159
  _globals['_SUBORDINATESERVICERREQUEST']._serialized_end=245
  _globals['_SERVICERESPONSE']._serialized_start=247
  _globals['_SERVICERESPONSE']._serialized_end=302
  _globals['_REQUESTPROMPT']._serialized_start=304
  _globals['_REQUESTPROMPT']._serialized_end=344
  _globals['_REQUESTLIST']._serialized_start=346
  _globals['_REQUESTLIST']._serialized_end=373
  _globals['_WORDLIST']._serialized_start=375
  _globals['_WORDLIST']._serialized_end=420
  _globals['_WORDVEC']._serialized_start=422
  _globals['_WORDVEC']._serialized_end=477
  _globals['_SENTENCEVEC']._serialized_start=479
  _globals['_SENTENCEVEC']._serialized_end=542
  _globals['_APMSERVICE']._serialized_start=545
  _globals['_APMSERVICE']._serialized_end=735
  _globals['_SUBFUNCTIONALSERVICE']._serialized_start=738
  _globals['_SUBFUNCTIONALSERVICE']._serialized_end=1028
# @@protoc_insertion_point(module_scope)
