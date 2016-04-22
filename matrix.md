
# SIMD operations

This table is generated automatically from [the
specification](portable-simd.md). For each SIMD type or interpretation, the
table indicates a **Y** when the operation has a definition specialized to this
interpretation.

When an operation is inherited from a less specific interpretation, that
interpretation is listed.


| Operation                   | b8x16 | b16x8 | b32x4 | b64x2 | s8x16 | s16x8 | s32x4 | s64x2 | u8x16 | u16x8 | u32x4 | u64x2 | f32x4 | f64x2 |
|-----------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| build                       |   Y   |   Y   |   Y   |   Y   | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| splat                       |   Y   |   Y   |   Y   |   Y   | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| extractLane                 |   Y   |   Y   |   Y   |   Y   | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| replaceLane                 |   Y   |   Y   |   Y   |   Y   | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| select                      |       |       |       |       | v8x16 | v16x8 | v32x4 | v64x2 | v8x16 | v16x8 | v32x4 | v64x2 | v32x4 | v64x2 |
| swizzle                     |       |       |       |       | v8x16 | v16x8 | v32x4 | v64x2 | v8x16 | v16x8 | v32x4 | v64x2 | v32x4 | v64x2 |
| shuffle                     |       |       |       |       | v8x16 | v16x8 | v32x4 | v64x2 | v8x16 | v16x8 | v32x4 | v64x2 | v32x4 | v64x2 |
| add                         |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| sub                         |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| mul                         |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| neg                         |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| addSaturate                 |       |       |       |       |   Y   |   Y   |       |       |   Y   |   Y   |       |       |       |       |
| subSaturate                 |       |       |       |       |   Y   |   Y   |       |       |   Y   |   Y   |       |       |       |       |
| shiftLeftByScalar           |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |       |       |
| shiftRightByScalar          |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |       |       |
| and                         |   Y   |   Y   |   Y   |   Y   |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |
| or                          |   Y   |   Y   |   Y   |   Y   |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |
| xor                         |   Y   |   Y   |   Y   |   Y   |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |
| not                         |   Y   |   Y   |   Y   |   Y   |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |  v128 |
| anyTrue                     |   Y   |   Y   |   Y   |   Y   |       |       |       |       |       |       |       |       |       |       |
| allTrue                     |   Y   |   Y   |   Y   |   Y   |       |       |       |       |       |       |       |       |       |       |
| equal                       |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| notEqual                    |       |       |       |       | i8x16 | i16x8 | i32x4 | i64x2 | i8x16 | i16x8 | i32x4 | i64x2 |   Y   |   Y   |
| lessThan                    |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| lessThanOrEqual             |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| greaterThan                 |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| greaterThanOrEqual          |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| abs                         |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| min                         |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| max                         |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| minNum                      |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| maxNum                      |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| div                         |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| sqrt                        |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| reciprocalApproximation     |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| reciprocalSqrtApproximation |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| fromSignedInt               |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| fromUnsignedInt             |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| fromFloat                   |       |       |       |       |       |       |   Y   |   Y   |       |       |   Y   |   Y   |       |       |
