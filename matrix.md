
# SIMD operations

This table is generated automatically from [the
specification](portable-simd.md). For each SIMD type or interpretation, the
table indicates:

* **Y** The operation has a definition specialized to this interpretation.
* **I** The operation has a definition for this interpretation that has been
inherited from a less specific interpretation. (e.g., `u32x4.add()` is inherited
from `i32x4.add()`).


| Operation                   |  v128 | b8x16 | b16x8 | b32x4 | b64x2 | v8x16 | v16x8 | v32x4 | v64x2 | i8x16 | i16x8 | i32x4 | i64x2 | s8x16 | s16x8 | s32x4 | s64x2 | u8x16 | u16x8 | u32x4 | u64x2 | f32x4 | f64x2 |
|-----------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| build                       |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| splat                       |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| extractLane                 |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| replaceLane                 |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| select                      |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| swizzle                     |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| shuffle                     |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| add                         |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| sub                         |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| mul                         |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| neg                         |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| addSaturate                 |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |       |       |   Y   |   Y   |       |       |       |       |
| subSaturate                 |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |       |       |   Y   |   Y   |       |       |       |       |
| shiftLeftByScalar           |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |       |       |
| shiftRightByScalar          |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |       |       |
| and                         |   Y   |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| or                          |   Y   |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| xor                         |   Y   |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| not                         |   Y   |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |
| anyTrue                     |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
| allTrue                     |       |   Y   |   Y   |   Y   |   Y   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
| equal                       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| notEqual                    |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   I   |   Y   |   Y   |
| lessThan                    |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| lessThanOrEqual             |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| greaterThan                 |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| greaterThanOrEqual          |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |   Y   |
| abs                         |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| min                         |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| max                         |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| minNum                      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| maxNum                      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| div                         |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| sqrt                        |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| reciprocalApproximation     |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| reciprocalSqrtApproximation |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |   Y   |
| fromInt32x4                 |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |       |
| fromInt64x2                 |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |
| fromUint32x4                |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |       |
| fromUint64x2                |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |
| fromFloat32x4               |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |       |       |       |   Y   |       |       |       |
| fromFloat64x2               |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |   Y   |       |       |       |   Y   |       |       |
