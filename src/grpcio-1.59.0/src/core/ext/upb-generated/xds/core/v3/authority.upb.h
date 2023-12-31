/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     xds/core/v3/authority.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#ifndef XDS_CORE_V3_AUTHORITY_PROTO_UPB_H_
#define XDS_CORE_V3_AUTHORITY_PROTO_UPB_H_

#include "upb/generated_code_support.h"
// Must be last. 
#include "upb/port/def.inc"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct xds_core_v3_Authority xds_core_v3_Authority;
extern const upb_MiniTable xds_core_v3_Authority_msg_init;



/* xds.core.v3.Authority */

UPB_INLINE xds_core_v3_Authority* xds_core_v3_Authority_new(upb_Arena* arena) {
  return (xds_core_v3_Authority*)_upb_Message_New(&xds_core_v3_Authority_msg_init, arena);
}
UPB_INLINE xds_core_v3_Authority* xds_core_v3_Authority_parse(const char* buf, size_t size, upb_Arena* arena) {
  xds_core_v3_Authority* ret = xds_core_v3_Authority_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &xds_core_v3_Authority_msg_init, NULL, 0, arena) != kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE xds_core_v3_Authority* xds_core_v3_Authority_parse_ex(const char* buf, size_t size,
                           const upb_ExtensionRegistry* extreg,
                           int options, upb_Arena* arena) {
  xds_core_v3_Authority* ret = xds_core_v3_Authority_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &xds_core_v3_Authority_msg_init, extreg, options, arena) !=
      kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE char* xds_core_v3_Authority_serialize(const xds_core_v3_Authority* msg, upb_Arena* arena, size_t* len) {
  char* ptr;
  (void)upb_Encode(msg, &xds_core_v3_Authority_msg_init, 0, arena, &ptr, len);
  return ptr;
}
UPB_INLINE char* xds_core_v3_Authority_serialize_ex(const xds_core_v3_Authority* msg, int options,
                                 upb_Arena* arena, size_t* len) {
  char* ptr;
  (void)upb_Encode(msg, &xds_core_v3_Authority_msg_init, options, arena, &ptr, len);
  return ptr;
}
UPB_INLINE void xds_core_v3_Authority_clear_name(xds_core_v3_Authority* msg) {
  const upb_MiniTableField field = {1, 0, 0, kUpb_NoSub, 9, (int)kUpb_FieldMode_Scalar | ((int)kUpb_FieldRep_StringView << kUpb_FieldRep_Shift)};
  _upb_Message_ClearNonExtensionField(msg, &field);
}
UPB_INLINE upb_StringView xds_core_v3_Authority_name(const xds_core_v3_Authority* msg) {
  upb_StringView default_val = upb_StringView_FromString("");
  upb_StringView ret;
  const upb_MiniTableField field = {1, 0, 0, kUpb_NoSub, 9, (int)kUpb_FieldMode_Scalar | ((int)kUpb_FieldRep_StringView << kUpb_FieldRep_Shift)};
  _upb_Message_GetNonExtensionField(msg, &field, &default_val, &ret);
  return ret;
}

UPB_INLINE void xds_core_v3_Authority_set_name(xds_core_v3_Authority *msg, upb_StringView value) {
  const upb_MiniTableField field = {1, 0, 0, kUpb_NoSub, 9, (int)kUpb_FieldMode_Scalar | ((int)kUpb_FieldRep_StringView << kUpb_FieldRep_Shift)};
  _upb_Message_SetNonExtensionField(msg, &field, &value);
}

extern const upb_MiniTableFile xds_core_v3_authority_proto_upb_file_layout;

#ifdef __cplusplus
}  /* extern "C" */
#endif

#include "upb/port/undef.inc"

#endif  /* XDS_CORE_V3_AUTHORITY_PROTO_UPB_H_ */
