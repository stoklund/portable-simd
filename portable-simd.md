# Portable SIMD

This specification describes a *Single Instruction Multiple Data* (SIMD)
instruction set that can be implemented efficiently on current popular
instruction set architectures. It provides shared semantics for
[WebAssembly][wasm] and [SIMD.js][simdjs].

# Types

The types used in this specification can be concrete or abstract. Concrete types
have a defined representation as a bit pattern, while abstract types are simple
a set of allowed values.

## Scalar types

The concrete scalar integer types are not interpreted as either signed or
unsigned integers.

* `i8`: An 8-bit integer with bits numbered 0–7.
* `i16`: A 16-bit integer with bits numbered 0–15.
* `i32`: A 32-bit integer with bits numbered 0–32.
* `i64`: A 64-bit integer with bits numbered 0–63.

The concrete scalar floating-point types follow the encoding and semantics of
the [IEEE 754-2008 standard for floating-point arithmetic][ieee754].

* `f32`: A floating-point number in the [IEEE][ieee754] *binary32* interchange
  format.
* `f64`: A floating-point number in the [IEEE][ieee754] *binary64* interchange
  format.

The following abstract types don't have a specified representation as a bit
pattern:

* `boolean`: Either `true` or `false`.
* `LaneIdx2`: An integer in the range 0–1 identifying a lane.
* `LaneIdx4`: An integer in the range 0–3 identifying a lane.
* `LaneIdx8`: An integer in the range 0–7 identifying a lane.
* `LaneIdx16`: An integer in the range 0–15 identifying a lane.
* `LaneIdx32`: An integer in the range 0–31 identifying a lane.

## SIMD types

All of the numerical SIMD types have a concrete mapping to a 128-bit
representation. The boolean types do not have a bit-pattern representation.

* `v128`: A 128-bit SIMD vector. Bits are numbered 0–127.
* `b8x16`: A vector of 16 `boolean` lanes numbered 0–15.
* `b16x8`: A vector of 8 `boolean` lanes numbered 0–7.
* `b32x4`: A vector of 4 `boolean` lanes numbered 0–3.
* `b64x2`: A vector of 2 `boolean` lanes numbered 0–1.

The `v128` type corresponds to a vector register in a typical ISA. The
interpretation of the 128 bits in the vector register is provided by the
individual instructions.

The abstract boolean vector types can be mapped to vector registers or predicate
registers by an implementation.

## Interpreting SIMD types

The single `v128` SIMD type can represent packed data in multiple ways.
Instructions specify how the bits should be interpreted through a hierarchy of
*interpretations*.

The boolean vector types only have the one interpretation given by their type.

### Lane division interpretation

The first level of interpretations of the `v128` type impose a lane structure on
the bits:

* `v8x16 : v128`: 8-bit lanes numbered 0–15. Lane n corresponds to bits 8n – 8n+7.
* `v16x8 : v128`: 16-bit lanes numbered 0–7. Lane n corresponds to bits 16n – 16n+15.
* `v32x4 : v128`: 32-bit lanes numbered 0–3. Lane n corresponds to bits 32n – 32n+31.
* `v64x2 : v128`: 64-bit lanes numbered 0–1. Lane n corresponds to bits 64n – 64n+63.

The lane divising interpretations don't say anything about the semantics of the
bits in each lane.

### Modulo integer interpretations

The bits in a lane can be interpreted as integers with modulo arithmetic
semantics. Many arithmetic operations can be defined on these types which don't
impose a signed or unsigned integer interpretation.

* `i8x16 : v8x16`: Each lane is an `i8`.
* `i16x8 : v16x8`: Each lane is an `i16`.
* `i32x4 : v32x4`: Each lane is an `i32`.
* `i64x2 : v64x2`: Each lane is an `i64`.

### Signed integer interpretations

Each lane is interpreted as a two's complement integer.

* `s8x16 : i8x16`: Lane values in the range -2^7 – 2^7-1.
* `s16x8 : i16x8`: Lane values in the range -2^15 – 2^15-1.
* `s32x4 : i32x4`: Lane values in the range -2^31 – 2^31-1.
* `s64x2 : i64x2`: Lane values in the range -2^63 – 2^63-1.

### Unsigned integer interpretations

Each lane is interpreted as an unsigned integer.

* `u8x16 : i8x16`: Lane values in the range 0 – 2^8-1.
* `u16x8 : i16x8`: Lane values in the range 0 – 2^16-1.
* `u32x4 : i32x4`: Lane values in the range 0 – 2^32-1.
* `u64x2 : i64x2`: Lane values in the range 0 – 2^64-1.

### Floating-point interpretations

Each lane is interpreted as an IEEE floating-point number.

* `f32x4 : v32x4`: Each lane is an `f32`.
* `f64x2 : v64x2`: Each lane is an `f64`.

# Operations

The SIMD operations described in this sections are generally named
`S.Op`, where `S` is either a SIMD type or one of the interpretations
of a SIMD type. The descriptions below refer to the following properties of `S`:

* `S.Lanes`: The number of lanes in the interpretation.
* `S.LaneBits`: The number of bits in each lane.
* `S.Reduce(x)`: For the integer interpretations: `x mod 2^S.LaneBits`.
* `S.Clamp(x)`: For the signed and unsigned integer interpretations, clamp `x`
  to the allowed value range for a lane.

## Constructing SIMD values

### Build vector from individual lanes
* `b8x16.build(x: boolean[16]) -> b8x16`
* `b16x8.build(x: boolean[8]) -> b16x8`
* `b32x4.build(x: boolean[4]) -> b32x4`
* `b64x2.build(x: boolean[2]) -> b64x2`
* `i8x16.build(x: i8[16]) -> v128`
* `i16x8.build(x: i16[8]) -> v128`
* `i32x4.build(x: i32[4]) -> v128`
* `i64x2.build(x: i64[2]) -> v128`
* `f32x4.build(x: f32[4]) -> v128`
* `f64x2.build(x: f64[2]) -> v128`

Construct a vector with `lane[i] = x[i]`.

### Create vector with identical lanes
* `b8x16.splat(x: boolean) -> b8x16`
* `b16x8.splat(x: boolean) -> b16x8`
* `b32x4.splat(x: boolean) -> b32x4`
* `b64x2.splat(x: boolean) -> b64x2`
* `i8x16.splat(x: i8) -> v128`
* `i16x8.splat(x: i16) -> v128`
* `i32x4.splat(x: i32) -> v128`
* `i64x2.splat(x: i64) -> v128`
* `f32x4.splat(x: f32) -> v128`
* `f64x2.splat(x: f64) -> v128`

Construct a vector with `x` replicated to all lanes: `lane[i] = x`.

## Accessing lanes

### Extract lane as a scalar
* `b8x16.extractLane(a: b8x16, i: LaneIdx16) -> boolean`
* `b16x8.extractLane(a: b16x8, i: LaneIdx8) -> boolean`
* `b32x4.extractLane(a: b32x4, i: LaneIdx4) -> boolean`
* `b64x2.extractLane(a: b64x2, i: LaneIdx2) -> boolean`
* `i8x16.extractLane(a: v128, i: LaneIdx16) -> i8`
* `i16x8.extractLane(a: v128, i: LaneIdx8) -> i16`
* `i32x4.extractLane(a: v128, i: LaneIdx4) -> i32`
* `i64x2.extractLane(a: v128, i: LaneIdx2) -> i64`
* `f32x4.extractLane(a: v128, i: LaneIdx4) -> f32`
* `f64x2.extractLane(a: v128, i: LaneIdx2) -> f64`

Extract the value of lane `i` in `a`.

### Replace lane value
* `b8x16.replaceLane(a: b8x16, i: LaneIdx16, x: boolean) -> b8x16`
* `b16x8.replaceLane(a: b16x8, i: LaneIdx8, x: boolean) -> b16x8`
* `b32x4.replaceLane(a: b32x4, i: LaneIdx4, x: boolean) -> b32x4`
* `b64x2.replaceLane(a: b64x2, i: LaneIdx2, x: boolean) -> b64x2`
* `i8x16.replaceLane(a: v128, i: LaneIdx16, x: i8) -> v128`
* `i16x8.replaceLane(a: v128, i: LaneIdx8, x: i16) -> v128`
* `i32x4.replaceLane(a: v128, i: LaneIdx4, x: i32) -> v128`
* `i64x2.replaceLane(a: v128, i: LaneIdx2, x: i64) -> v128`
* `f32x4.replaceLane(a: v128, i: LaneIdx4, x: f32) -> v128`
* `f64x2.replaceLane(a: v128, i: LaneIdx2, x: f64) -> v128`

Return a new vector with lanes identical to `a`, except for lane `i` which has
the value `x`.

### Lane-wise select
* `v8x16.select(s: b8x16, t: v128, f: v128) -> v128`
* `v16x8.select(s: b16x8, t: v128, f: v128) -> v128`
* `v32x4.select(s: b32x4, t: v128, f: v128) -> v128`
* `v64x2.select(s: b64x2, t: v128, f: v128) -> v128`

Create vector with `lane[i] = s[i] ? t[i] : f[i]`.

### Swizzle lanes
* `v8x16.swizzle(a: v128, s: LaneIdx16[16]) -> v128`
* `v16x8.swizzle(a: v128, s: LaneIdx8[8]) -> v128`
* `v32x4.swizzle(a: v128, s: LaneIdx4[4]) -> v128`
* `v64x2.swizzle(a: v128, s: LaneIdx2[2]) -> v128`

Create vector with `lane[i] = a[s[i]]`.

### Shuffle lanes
* `v8x16.shuffle(a: v128, b: v128, s: LaneIdx32[16]) -> v128`
* `v16x8.shuffle(a: v128, b: v128, s: LaneIdx16[8]) -> v128`
* `v32x4.shuffle(a: v128, b: v128, s: LaneIdx8[4]) -> v128`
* `v64x2.shuffle(a: v128, b: v128, s: LaneIdx4[2]) -> v128`

Create vector with `lane[i] = s[i] < S.lanes ? a[s[i]] : b[s[i] - S.lanes]`.

## Integer arithmetic

### Integer addition
* `i8x16.add(a: v128, b: v128) -> v128`
* `i16x8.add(a: v128, b: v128) -> v128`
* `i32x4.add(a: v128, b: v128) -> v128`
* `i64x2.add(a: v128, b: v128) -> v128`

Lane-wise wrapping integer addition: `lane[i] = S.Reduce(a[i] + b[i])`.

### Integer subtraction
* `i8x16.sub(a: v128, b: v128) -> v128`
* `i16x8.sub(a: v128, b: v128) -> v128`
* `i32x4.sub(a: v128, b: v128) -> v128`
* `i64x2.sub(a: v128, b: v128) -> v128`

Lane-wise wrapping integer subtraction: `lane[i] = S.Reduce(a[i] - b[i])`.

### Integer multiplication
* `i8x16.mul(a: v128, b: v128) -> v128`
* `i16x8.mul(a: v128, b: v128) -> v128`
* `i32x4.mul(a: v128, b: v128) -> v128`
* `i64x2.mul(a: v128, b: v128) -> v128`

Lane-wise wrapping integer multiplication: `lane[i] = S.Reduce(a[i] * b[i])`.

### Integer negation
* `i8x16.neg(a: v128) -> v128`
* `i16x8.neg(a: v128) -> v128`
* `i32x4.neg(a: v128) -> v128`
* `i64x2.neg(a: v128) -> v128`

Lane-wise wrapping integer negation: `lane[i] = S.Reduce(-a[i])`. In wrapping
arithmetic, `y = -x` is the unique value such that `x + y == 0`.

## Saturating integer arithmetic

Saturating integer arithmetic behaves differently on signed and unsigned types.
It is only defined for 8-bit and 16-bit integer lanes.

### Saturating integer addition
* `s8x16.addSaturate(a: v128, b: v128) -> v128`
* `s16x8.addSaturate(a: v128, b: v128) -> v128`
* `u8x16.addSaturate(a: v128, b: v128) -> v128`
* `u16x8.addSaturate(a: v128, b: v128) -> v128`

Lane-wise saturating addition: `lane[i] = S.Clamp(a[i] + b[i])`.

### Saturating integer subtraction
* `s8x16.subSaturate(a: v128, b: v128) -> v128`
* `s16x8.subSaturate(a: v128, b: v128) -> v128`
* `u8x16.subSaturate(a: v128, b: v128) -> v128`
* `u16x8.subSaturate(a: v128, b: v128) -> v128`

Lane-wise saturating subtraction: `lane[i] = S.Clamp(a[i] - b[i])`.

## Bit shifts

### Left shift by scalar
* `i8x16.shiftLeftByScalar(a: v128, b: i8) -> v128`
* `i16x8.shiftLeftByScalar(a: v128, b: i8) -> v128`
* `i32x4.shiftLeftByScalar(a: v128, b: i8) -> v128`
* `i64x2.shiftLeftByScalar(a: v128, b: i8) -> v128`

Shift the bits in each lane to the left by the same amount. Only the low bits of
the shift amount are used:

    bits = b mod S.LaneBits
    lane[i] = S.Reduce(a[i] * 2^bits)

### Right shift by scalar
* `s8x16.shiftRightByScalar(a: v128, b: i8) -> v128`
* `s16x8.shiftRightByScalar(a: v128, b: i8) -> v128`
* `s32x4.shiftRightByScalar(a: v128, b: i8) -> v128`
* `s64x2.shiftRightByScalar(a: v128, b: i8) -> v128`
* `u8x16.shiftRightByScalar(a: v128, b: i8) -> v128`
* `u16x8.shiftRightByScalar(a: v128, b: i8) -> v128`
* `u32x4.shiftRightByScalar(a: v128, b: i8) -> v128`
* `u64x2.shiftRightByScalar(a: v128, b: i8) -> v128`

Shift the bits in each lane to the right by the same amount. This is an
arithmetic right shift for the signed integer interpretations and a logical
right shift for the unsigned integer interpretations.

    bits = b mod S.LaneBits
    lane[i] = truncate_toward_negative(a[i] / 2^bits)

## Logical operations

The logical operations are defined on the boolean types and the `v128` type
where they operate on the individual bits.

### Logical and
* `v128.and(a: v128, b: v128) -> v128`
* `b8x16.and(a: b8x16, b: b8x16) -> b8x16`
* `b16x8.and(a: b16x8, b: b16x8) -> b16x8`
* `b32x4.and(a: b32x4, b: b32x4) -> b32x4`
* `b64x2.and(a: b64x2, b: b64x2) -> b64x2`

### Logical or
* `v128.or(a: v128, b: v128) -> v128`
* `b8x16.or(a: b8x16, b: b8x16) -> b8x16`
* `b16x8.or(a: b16x8, b: b16x8) -> b16x8`
* `b32x4.or(a: b32x4, b: b32x4) -> b32x4`
* `b64x2.or(a: b64x2, b: b64x2) -> b64x2`

### Logical xor
* `v128.xor(a: v128, b: v128) -> v128`
* `b8x16.xor(a: b8x16, b: b8x16) -> b8x16`
* `b16x8.xor(a: b16x8, b: b16x8) -> b16x8`
* `b32x4.xor(a: b32x4, b: b32x4) -> b32x4`
* `b64x2.xor(a: b64x2, b: b64x2) -> b64x2`

### Logical not
* `v128.not(a: v128) -> v128`
* `b8x16.not(a: b8x16) -> b8x16`
* `b16x8.not(a: b16x8) -> b16x8`
* `b32x4.not(a: b32x4) -> b32x4`
* `b64x2.not(a: b64x2) -> b64x2`

## Boolean reductions

### Any lane true
* `b8x16.anyTrue(a: b8x16) -> boolean`
* `b16x8.anyTrue(a: b16x8) -> boolean`
* `b32x4.anyTrue(a: b32x4) -> boolean`
* `b64x2.anyTrue(a: b64x2) -> boolean`

These functions return true if any lane in `a` is true.

### All lanes true
* `b8x16.allTrue(a: b8x16) -> boolean`
* `b16x8.allTrue(a: b16x8) -> boolean`
* `b32x4.allTrue(a: b32x4) -> boolean`
* `b64x2.allTrue(a: b64x2) -> boolean`

These functions return true if all lanes in `a` are true.

## Comparisons

The comparison operations all compare two vectors lane-wise, and produce a
boolean vector with the same number of lanes as the input interpretation.

### Equality
* `i8x16.equal(a: v128, b: v128) -> b8x16`
* `i16x8.equal(a: v128, b: v128) -> b16x8`
* `i32x4.equal(a: v128, b: v128) -> b32x4`
* `i64x2.equal(a: v128, b: v128) -> b64x2`
* `f32x4.equal(a: v128, b: v128) -> b32x4`
* `f64x2.equal(a: v128, b: v128) -> b64x2`

Integer equality is independent of the signed/unsigned interpretation. Floating
point equality follows IEEE semantics, so a NaN lane compares not equal with
anything, including itself: `lane[i] = (a[i] == b[i])`.

### Non-equality
* `i8x16.notEqual(a: v128, b: v128) -> b8x16`
* `i16x8.notEqual(a: v128, b: v128) -> b16x8`
* `i32x4.notEqual(a: v128, b: v128) -> b32x4`
* `i64x2.notEqual(a: v128, b: v128) -> b64x2`
* `f32x4.notEqual(a: v128, b: v128) -> b32x4`
* `f64x2.notEqual(a: v128, b: v128) -> b64x2`

The `notEqual` operations produce the inverse of their `equal` counterparts:
`lane[i] = (a[i] != b[i])`.

### Less than
* `s8x16.lessThan(a: v128, b: v128) -> b8x16`
* `s16x8.lessThan(a: v128, b: v128) -> b16x8`
* `s32x4.lessThan(a: v128, b: v128) -> b32x4`
* `s64x2.lessThan(a: v128, b: v128) -> b64x2`
* `u8x16.lessThan(a: v128, b: v128) -> b8x16`
* `u16x8.lessThan(a: v128, b: v128) -> b16x8`
* `u32x4.lessThan(a: v128, b: v128) -> b32x4`
* `u64x2.lessThan(a: v128, b: v128) -> b64x2`
* `f32x4.lessThan(a: v128, b: v128) -> b32x4`
* `f64x2.lessThan(a: v128, b: v128) -> b64x2`

Integer magnitude comparisons depend on the signed/unsigned interpretation of
the lanes. Floating point comparisons follow IEEE semantics: `lane[i] = (a[i] <
b[i])`.

### Less than or equal
* `s8x16.lessThanOrEqual(a: v128, b: v128) -> b8x16`
* `s16x8.lessThanOrEqual(a: v128, b: v128) -> b16x8`
* `s32x4.lessThanOrEqual(a: v128, b: v128) -> b32x4`
* `s64x2.lessThanOrEqual(a: v128, b: v128) -> b64x2`
* `u8x16.lessThanOrEqual(a: v128, b: v128) -> b8x16`
* `u16x8.lessThanOrEqual(a: v128, b: v128) -> b16x8`
* `u32x4.lessThanOrEqual(a: v128, b: v128) -> b32x4`
* `u64x2.lessThanOrEqual(a: v128, b: v128) -> b64x2`
* `f32x4.lessThanOrEqual(a: v128, b: v128) -> b32x4`
* `f64x2.lessThanOrEqual(a: v128, b: v128) -> b64x2`

Semantics: `lane[i] = (a[i] <= b[i])`.

### Greater than
* `s8x16.greaterThan(a: v128, b: v128) -> b8x16`
* `s16x8.greaterThan(a: v128, b: v128) -> b16x8`
* `s32x4.greaterThan(a: v128, b: v128) -> b32x4`
* `s64x2.greaterThan(a: v128, b: v128) -> b64x2`
* `u8x16.greaterThan(a: v128, b: v128) -> b8x16`
* `u16x8.greaterThan(a: v128, b: v128) -> b16x8`
* `u32x4.greaterThan(a: v128, b: v128) -> b32x4`
* `u64x2.greaterThan(a: v128, b: v128) -> b64x2`
* `f32x4.greaterThan(a: v128, b: v128) -> b32x4`
* `f64x2.greaterThan(a: v128, b: v128) -> b64x2`

Semantics: `lane[i] = (a[i] > b[i])`.

### Greater than or equal
* `s8x16.greaterThanOrEqual(a: v128, b: v128) -> b8x16`
* `s16x8.greaterThanOrEqual(a: v128, b: v128) -> b16x8`
* `s32x4.greaterThanOrEqual(a: v128, b: v128) -> b32x4`
* `s64x2.greaterThanOrEqual(a: v128, b: v128) -> b64x2`
* `u8x16.greaterThanOrEqual(a: v128, b: v128) -> b8x16`
* `u16x8.greaterThanOrEqual(a: v128, b: v128) -> b16x8`
* `u32x4.greaterThanOrEqual(a: v128, b: v128) -> b32x4`
* `u64x2.greaterThanOrEqual(a: v128, b: v128) -> b64x2`
* `f32x4.greaterThanOrEqual(a: v128, b: v128) -> b32x4`
* `f64x2.greaterThanOrEqual(a: v128, b: v128) -> b64x2`

Semantics: `lane[i] = (a[i] >= b[i])`.


## Load and store
## Floating-point arithmetic


[wasm]: https://webassembly.github.io/ (WebAssembly)
[simdjs]: http://tc39.github.io/ecmascript_simd/ (SIMD.js specification)
[ieee754]: https://standards.ieee.org/findstds/standard/754-2008.html (754-2008 - IEEE Standard for Floating-Point Arithmetic)
