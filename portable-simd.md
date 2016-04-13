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
* `LaneIdx`: A non-negative integer identifying a lane in a SIMD vector. The
  valid range depends on the vector typed being indexes. Lane
  indexes are always immediate operands on instructions, so dynamic range
  checking is not an issue.

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

### Lane division interpretation

The first level of interpretations of the `v128` type impose a lane structure on
the bits:

* `v8x16 : v128`: 8-bit lanes numbered 0–15. Lane n corresponds to bits 8n – 8n+7.
* `v8x16 : v128`: 16-bit lanes numbered 0–7. Lane n corresponds to bits 16n – 16n+15.
* `v32x4 : v128`: 32-bit lanes numbered 0–3. Lane n corresponds to bits 32n – 32n+31.
* `v64x2 : v128`: 64-bit lanes numbered 0–1. Lane n corresponds to bits 64n – 64n+63.

The lane divising interpretations don't say anything about the semantics of the
bits in each lane.

### Modulo integer interpretations

The bits in a lane can be interpreted as integers with modulo arithmetic
semantics. Many arithmetic operations can be defined on these types which don't
impose a signed or unsigned integer interpretation.

* `i8x16 : v8x16`: Each lane is an `i8`.
* `i8x16 : v16x8`: Each lane is an `i16`.
* `i32x4 : v32x4`: Each lane is an `i32`.
* `i64x2 : v64x2`: Each lane is an `i64`.

### Signed integer interpretations

Each lane is interpreted as a two's complement integer.

* `s8x16 : i8x16`: Lane values in the range -2^7 – 2^7-1.
* `s8x16 : i16x8`: Lane values in the range -2^15 – 2^15-1.
* `s32x4 : i32x4`: Lane values in the range -2^31 – 2^31-1.
* `s64x2 : i64x2`: Lane values in the range -2^63 – 2^63-1.

### Unsigned integer interpretations

Each lane is interpreted as an unsigned integer.

* `u8x16 : i8x16`: Lane values in the range 0 – 2^8-1.
* `u8x16 : i16x8`: Lane values in the range 0 – 2^16-1.
* `u32x4 : i32x4`: Lane values in the range 0 – 2^32-1.
* `u64x2 : i64x2`: Lane values in the range 0 – 2^64-1.

### Floating-point interpretations

Each lane is interpreted as an IEEE floating-point number.

* `f32x4 : v32x4`: Each lane is an `f32`.
* `f64x2 : v64x2`: Each lane is an `f64`.


[wasm]: https://webassembly.github.io/ (WebAssembly)
[simdjs]: http://tc39.github.io/ecmascript_simd/ (SIMD.js specification)
[ieee754]: https://standards.ieee.org/findstds/standard/754-2008.html (754-2008 - IEEE Standard for Floating-Point Arithmetic)
