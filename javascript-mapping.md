# Language mapping for JavaScript

SIMD.js defines primitive SIMD types with a `[[SIMDElements]]` field containing
one of the types from the portable SIMD specification. The corresponding SIMD
type descriptors have an `[[Interpretation]]` field referencing one of the SIMD
interpretations in this spec.

| Constructor    | `[[SIMDElements]]` type | `[[Interpretation]]` |
|----------------|:-----------------------:|:--------------------:|
| SIMD.Float32x4 | `v128`                  | `f32x4`              |
| SIMD.Int32x4   | `v128`                  | `s32x4`              |
| SIMD.Int16x8   | `v128`                  | `s16x8`              |
| SIMD.Int8x16   | `v128`                  | `s8x16`              |
| SIMD.Uint32x4  | `v128`                  | `u32x4`              |
| SIMD.Uint16x8  | `v128`                  | `u16x8`              |
| SIMD.Uint8x16  | `v128`                  | `u8x16`              |
| SIMD.Bool32x4  | `b32x4`                 | `b32x4`              |
| SIMD.Bool16x8  | `b16x4`                 | `b16x8`              |
| SIMD.Bool8x16  | `b8x16`                 | `b8x16`              |

SIMD.js does not currently provide mappings for any of the 64x2 types.

## Abstract operations

### SIMDCreate(descriptor, elements)

1. Return the SIMD value specified by the record { [[SIMDTypeDescriptor]]: descriptor, [[SIMDElements]]: elements }.

### SIMDUnaryOp(a, op, descriptor)

1. If `a.[[SIMDTypeDescriptor]]` is not `descriptor`, throw a TypeError exception.
2. Let `res` be `descriptor.[[Interpretation]].op(a.[[SIMDElements]])`.
3. Return `SIMDCreate(descriptor, res)`.

### SIMDBinaryOp(a, b, op, descriptor, outputDescriptor)

1. If `a.[[SIMDTypeDescriptor]]` is not `descriptor` or `b.[[SIMDTypeDescriptor]]` is not `descriptor`, throw a TypeError exception.
2. If `outputDescriptor` is not provided, let `outputDescriptor` be `descriptor`.
3. Let `res` be `descriptor.[[Interpretation]].op(a.[[SIMDElements]], b.[[SIMDElements]])`.
4. Return `SIMDCreate(outputDescriptor, res)`.

### SIMDRelationalOp(a, b, op, descriptor)

1. Let `outputDescriptor` be `SIMDBoolType(descriptor)`.
2. Return `SIMDBinaryOp(a, b, op, descriptor, outputDescriptor)`.

### SIMDScalarOp(a, bits, op, descriptor)

1. If `a.[[SIMDTypeDescriptor]]` is not `descriptor`, throw a TypeError exception.
2. Let `scalar` be `ToUint8(bits)`.
3. Let `res` be `descriptor.[[Interpretation]].op(a.[[SIMDElements]], scalar)`.
4. Return `SIMDCreate(descriptor, res)`.

## Properties of the SIMDConstructor constructors

### Unary operations

The unary operations listed in the table below are defined as properties
`«SIMD»Constructor.«Operation»(a)` where `«SIMD»` is one of the SIMD types and
`«Operation»` is the name of the operation.

1. Let `result` be `SIMDUnaryOp(a, «Operation», «SIMD»Descriptor)`.
2. ReturnIfAbrupt(`result`).
3. Return `result`.

| `«Operation»`               | SIMD types supported       |
|-----------------------------|----------------------------|
| neg                         | integer and floating-point |
| sqrt                        | floating-point             |
| reciprocalSqrtApproximation | floating-point             |
| reciprocalApproximation     | floating-point             |
| abs                         | floating-point             |
| not                         | integer and boolean        |

### Binary operations

The unary operations listed in the table below are defined as properties
`«SIMD»Constructor.«Operation»(a, b)` where `«SIMD»` is one of the SIMD types and
`«Operation»` is the name of the operation.

1. Let `result` be `SIMDBinaryOp(a, b, «Operation», «SIMD»Descriptor)`.
2. ReturnIfAbrupt(`result`).
3. Return `result`.

| `«Operation»`               | SIMD types supported       |
|-----------------------------|----------------------------|
| add                         | integer and floating-point |
| sub                         | integer and floating-point |
| mul                         | integer and floating-point |
| div                         | floating-point             |
| max                         | floating-point             |
| min                         | floating-point             |
| maxNum                      | floating-point             |
| minNum                      | floating-point             |
| and                         | integer and boolean        |
| xor                         | integer and boolean        |
| or                          | integer and boolean        |
| addSaturate                 | 8x16 and 16x8 integers     |
| subSaturate                 | 8x16 and 16x8 integers     |

### Relational operations

The relational operations listed in the table below are defined as properties
`«SIMD»Constructor.«Operation»(a, b)` where `«SIMD»` is one of the SIMD types
and `«Operation»` is the name of the operation.

1. Let `result` be `SIMDRelationalOp(a, b, «Operation», «SIMD»Descriptor)`.
2. ReturnIfAbrupt(`result`).
3. Return `result`.

| `«Operation»`               | SIMD types supported       |
|-----------------------------|----------------------------|
| lessThan                    | integer and floating-point |
| lessThanOrEqual             | integer and floating-point |
| greaterThan                 | integer and floating-point |
| greaterThanOrEqual          | integer and floating-point |
| equal                       | integer and floating-point |
| notEqual                    | integer and floating-point |

### «SIMD»Constructor.anyTrue(a)

This operation is only defined on boolean SIMD types.

1. If `a.[[SIMDTypeDescriptor]]` is not `«SIMD»Descriptor`, throw a TypeError exception.
2. Return `«SIMD»Descriptor.[[Interpretation]].anyTrue(a.[[SIMDElements]])`.

### «SIMD»Constructor.shiftLeftByScalar(a, bits)

This operation is only defined on integer SIMD types.

2. Let `result` be `SIMDScalarOp(a, bits, shiftLeftByScalar, «SIMD»Descriptor)`.
3. ReturnIfAbrupt(`result`).
4. Return `result`.

### «SIMD»Constructor.shuffle(a, b, ...lanes)

This operation exists only on integer and floating point SIMD types.

1. If `a.[[SIMDTypeDescriptor]]` is not `«SIMD»Descriptor`, or if
   `b.[[SIMDTypeDescriptor]]` is not `«SIMD»Descriptor`, throw a TypeError
   exception.
2. Let `indices` be a new `List`.
    1.  For integer `n` from 0 to `«SIMD»Descriptor.[[VectorLength]]`,
        1. Let `lane` be `lanes[i]`, or 0 if lanes is not long enough.
        2. Let `index` be `SIMDToLane(«SIMD»Descriptor.[[VectorLength]] * 2, lane)`.
        3. ReturnIfAbrupt(`index`).
        4. Append `index` to the end of `indices`.
3. Let `res` be `«SIMD»Descriptor.[[Interpretation]].shuffle(a, b, indices)`.
4. Return `SIMDCreate(«SIMD»Descriptor, res)`.

### 
