# SIMD support for WebAssembly

This document describes how SIMD types and operations can be added to
WebAssembly by referencing the [portable SIMD specification](portable-simd.md).

## SIMD types

The following value types are added to the WebAssembly type system to support
128-bit SIMD operations. Each new WebAssembly value type corresponds to the
[portable SIMD type](portable-simd.md#simd-types) of the same name.

* `v128`: A 128-bit SIMD vector.
* `b8x16`: A vector of 16 boolean lanes.
* `b16x8`: A vector of 8 boolean lanes.
* `b32x4`: A vector of 4 boolean lanes.
* `b64x2`: A vector of 2 boolean lanes.

## Scalar type mappings

Some operations in the portable SIMD specification use scalar types that don't
exist in WebAssembly. These types are mapped into WebAssembly as follows:

* `i8` and `i16`: SIMD operations that take these types as an input are passed
  a WebAssembly `i32` instead and use only the low bits. The `extractLane`
  operation can return these types. It is provided in variants that either
  sign-extend or zero-extend to an `i32`.

* `boolean`: SIMD operations with a boolean argument will accept a WebAssembly
  `i32` instead and treat zero as false and non-zero values as true. SIMD
  operations that return a boolean will return an `i32` with the value 0 or 1.

* `LaneIdx2` through `LaneIdx32`: All lane indexes are encoded as immediate
  operands. Dynamic lane indexes are not used anywhere, so they don't need to be
  mapped to the WebAssembly type system.

* `RoundingMode`: Rounding modes are encoded as immediate operands. There is
  no mapping to the WebAssembly type system.

## SIMD operations

Most operation names are simply mapped from their portable SIMD versions. Some
are renamed to match existing operations. The integer operations that
distinguish between signed and unsigned integers are given `_s` or `_u`
suffixes. For example, `s32x4.greaterThan` becomes `i32x4.gt_s`, c.f. the
existing `i32.gt_s` WebAssembly operation.

### Simply mapped operations

The following operations are mapped trivially from their portable SIMD
specification to the WebAssembly types.

These are the simply mapped operations:
* `select`, `swizzle`, `shuffle`.
* `add`, `sub`, `mul`, `neg`.
* `shiftLeftByScalar`.
* `and`, `or`, `xor`, `not`.
* `anyTrue`, `allTrue`.
* `equal`, `notEqual`.
* `neg`, `abs`.
* `min`, `max`.
* `div`, `sqrt`.
* `reciprocalApproximation`, `reciprocalSqrtApproximation`.

Note that these operations are *not* mapped: `minNum`, `maxNum`.

### Signed/unsigned integer operations

These operations are defined on the signed and unsigned interpretations
separately. They are mapped to the WebAssembly `v128` type by adding `_s` and
`_u` suffixes for signed and unsigned operations respectively. For example:

* `i8x16.shiftRightByScalar_u(a: v128, y: i32) -> v128`
* `i8x16.shiftRightByScalar_s(a: v128, y: i32) -> v128`
* `i16x8.shiftRightByScalar_u(a: v128, y: i32) -> v128`
* `i16x8.shiftRightByScalar_s(a: v128, y: i32) -> v128`
* `i32x4.shiftRightByScalar_u(a: v128, y: i32) -> v128`
* `i32x4.shiftRightByScalar_s(a: v128, y: i32) -> v128`
* `i64x2.shiftRightByScalar_u(a: v128, y: i32) -> v128`
* `i64x2.shiftRightByScalar_s(a: v128, y: i32) -> v128`

The following signed/unsigned operations are mapped:

* `lessThan`, `lessThanOrEqual`.
* `greaterThan`, `greaterThanOrEqual`.
* `shiftRightByScalar`.
* `addSaturate`, `subSaturate`.

### Conversions

The `fromSignedInt` and `fromUnsignedInt` conversions to float never fail, so
they are simply renamed:

* `f32x4.convert_s/i32x4(a: v128, rmode: RoundingMode) -> v128`
* `f64x2.convert_s/i64x2(a: v128, rmode: RoundingMode) -> v128`
* `f32x4.convert_u/i32x4(a: v128, rmode: RoundingMode) -> v128`
* `f64x2.convert_u/i64x2(a: v128, rmode: RoundingMode) -> v128`

The float to integer conversions can fail. Conversion failure is converted to a
trap, same as the scalar WebAssembly conversions:

* `i32x4.trunc_s/f32x4(a: v128) -> v128`
* `i64x2.trunc_s/f64x2(a: v128) -> v128`
* `i32x4.trunc_u/f32x4(a: v128) -> v128`
* `i64x2.trunc_u/f64x2(a: v128) -> v128`

## Memory operations

The load and store operations use the same addressing and bounds checking as the
scalar WebAssembly memory instructions, and effective addresses are provided in
the same way by a dynamic address and an immediate offset operand.

Since WebAssembly is always little-endian, the `load` and `store` instructions
are not dependent on the lane-wise interpretation of the vector being loaded or
stored. This means that there are only two instructions:

* `v128.load(addr, offset) -> v128`
* `v128.store(addr, offset, data: v128)`

The partial vector load/store instructions are specific to the 4-lane
interpretation:

* `v32x4.load1(addr, offset) -> v128`
* `v32x4.load2(addr, offset) -> v128`
* `v32x4.load3(addr, offset) -> v128`
* `v32x4.store1(addr, offset, data: v128)`
* `v32x4.store2(addr, offset, data: v128)`
* `v32x4.store3(addr, offset, data: v128)`
