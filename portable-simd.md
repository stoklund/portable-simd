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

* `i8`: An 8-bit integer with bits numbered 0–7 from the LSB.
* `i16`: A 16-bit integer with bits numbered 0–15 from the LSB.
* `i32`: A 32-bit integer with bits numbered 0–32 from the LSB.
* `i64`: A 64-bit integer with bits numbered 0–63 from the LSB.

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


[wasm]: https://webassembly.github.io/ (WebAssembly)
[simdjs]: http://tc39.github.io/ecmascript_simd/ (SIMD.js specification)
[ieee754]: https://standards.ieee.org/findstds/standard/754-2008.html (754-2008 - IEEE Standard for Floating-Point Arithmetic)
