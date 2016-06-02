# SIMD support for WebAssembly

This document describes how SIMD types and operations can be added to
WebAssembly by referencing the [portable SIMD specification](portable-simd.md).

## SIMD types

The following types are added to the WebAssembly type system to support 128-bit
SIMD operations. Each new Wasm type is mapped to one of the portable SIMD types
and possibly one or more interpretations of that type.

| Wasm    | SIMD    | Interpretations  |
|---------|---------|------------------|
| `i8x16` | `v128`  | `s8x16`, `u8x16` |
| `i16x8` | `v128`  | `s16x8`, `u16x8` |
| `i32x4` | `v128`  | `s32x4`, `u32x4` |
| `i64x2` | `v128`  | `s64x2`, `u64x2` |
| `f32x4` | `v128`  | `f32x4`          |
| `f64x2` | `v128`  | `f64x2`          |
| `b8x16` | `b8x16` |                  |
| `b16x8` | `b16x8` |                  |
| `b32x4` | `b32x4` |                  |
| `b64x2` | `b64x2` |                  |

Just like the scalar types `i32` and `i64`, WebAssembly SIMD types do not
distinguish between signed and unsigned integers.

## Scalar type mappings

Some operations in the portable SIMD specification use scalar types that don't
exist in WebAssembly. These types are mapped into WebAssembly as follows:

* `i8` and `i16`: SIMD operations that take these types as input are passed a
  Wasm `i32` instead and use only the low bits. The `extractLane` operation can
  return these types. It will provided in variants that either sign-extend or
  zero-extend to an `i32`.

* `boolean`: SIMD operations with a boolean argument will accept a Wasm `i32`
  instead and treat zero as false and non-zero values as true. SIMD operations
  that return a boolean wil return an `i32` with the value 0 or 1.

* `LaneIdx2` through `LaneIdx32`: All lane indexes are encoded as immediate
  operands. Dynamic lane indexes are not used anywhere, so they don't need to be
  mapped to the WebAssembly type system.

* `RoundingMode`: Rounding modes are encoded as immediate operands. There is
  no mapping to the WebAssembly type system.

## Reinterpretations

The 6 WebAssembly types that map to the `v128` SIMD type have reinterpretation
operators that cast their `v128` value as a different type without changing the
bits in the `v128` value. There is a total of 6 x 5 = 30 SIMD reinterpretation
opcodes:

* `i8x16.reinterpret/i16x8`: reinterpret an `i16x8` as an `i8x16`.
* `i8x16.reinterpret/i32x4`: ...
* `i8x16.reinterpret/i64x2`: ...
* `i8x16.reinterpret/f32x4`: ...
* `i8x16.reinterpret/f64x2`: ...
* `i16x8.reinterpret/i8x16`: ...
* ...
* `f64x2.reinterpret/f32x4`: ...

The boolean SIMD types cannot be reinterpreted.

## SIMD operations

All types support the `build` constructor, but since WebAssembly doesn't have
array types, the individual lane values are provided as N scalar arguments for
an N-lane type.

All types support `splat` and `replaceLane` with the scalar type mapping
described above.

The `i8x16` and `i16x8` types have two `extractLane` variants:

* `i8x16.extractLane_u(a: i8x16, i: LaneIdx16) -> u32`
  Zero-extend `i8` lane to `i32`.
* `i8x16.extractLane_s(a: i8x16, i: LaneIdx16) -> u32`
  Sign-extend `i8` lane to `i32`.
* `i16x8.extractLane_u(a: i16x8, i: LaneIdx8) -> u32`
  Zero-extend `i16` lane to `i32`.
* `i16x8.extractLane_s(a: i16x8, i: LaneIdx8) -> u32`
  Sign-extend `i16` lane to `i32`.

All other types have a single `extractLane` operation with the standard scalar
type mapping, so the boolean versions return `i32` with a value of 0 or 1.

### Simply mapped operations

The following operations are mapped trivially from their portable SIMD
specification to the WebAssembly types. An operation is defined for a
WebAssembly type if it is specified for the Wasm type's mapped SIMD type or one
of its interpretations. For example, the `i32x4` Wasm type gets the operations
defined on these SIMD interpretations: `s32x4`, `u32x4`, `i32x4`, `v32x4`, and
`v128`.

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
separately. They are mapped to the WebAssembly integer SIMD types by adding `_s`
and `_u` suffixes for signed and unsigned operations respectively. For example:

* `i8x16.shiftRightByScalar_u(a: i8x16, y: i32) -> i8x16`
* `i8x16.shiftRightByScalar_s(a: i8x16, y: i32) -> i8x16`
* `i16x8.shiftRightByScalar_u(a: i16x8, y: i32) -> i16x8`
* `i16x8.shiftRightByScalar_s(a: i16x8, y: i32) -> i16x8`
* `i32x4.shiftRightByScalar_u(a: i32x4, y: i32) -> i32x4`
* `i32x4.shiftRightByScalar_s(a: i32x4, y: i32) -> i32x4`
* `i64x2.shiftRightByScalar_u(a: i64x2, y: i32) -> i64x2`
* `i64x2.shiftRightByScalar_s(a: i64x2, y: i32) -> i64x2`

The following signed/unsigned operations are mapped:

* `lessThan`, `lessThanOrEqual`.
* `greaterThan`, `greaterThanOrEqual`.
* `shiftRightByScalar`.
* `addSaturate`, `subSaturate`.

### Conversions

The `fromSignedInt` and `fromUnsignedInt` conversions to float never fail, so
they are simply renamed:

* `f32x4.convert_s/i32x4(a: i32x4, rmode: RoundingMode) -> f32x4`
* `f64x2.convert_s/i64x2(a: i64x2, rmode: RoundingMode) -> f64x2`
* `f32x4.convert_u/i32x4(a: i32x4, rmode: RoundingMode) -> f32x4`
* `f64x2.convert_u/i64x2(a: i64x2, rmode: RoundingMode) -> f64x2`

The float to integer conversions can fail. Conversion failure is converted to a
trap, same as the scalar WebAssembly conversions:

* `i32x4.trunc_s/f32x4(a: f32x4) -> i32x4`
* `i64x2.trunc_s/f64x2(a: f64x2) -> i64x2`
* `i32x4.trunc_u/f32x4(a: f32x4) -> i32x4`
* `i64x2.trunc_u/f64x2(a: f64x2) -> i64x2`

## Memory operations

The load and store operations use the same addressing and bounds checking as the
scalar WebAssembly memory instructions. All the numerical types support the
`load` and `store` instructions, while the partial operations are only supported
by the 32x4 types.
