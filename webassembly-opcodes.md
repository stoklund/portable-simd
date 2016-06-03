
# WebAssembly SIMD operations

This table is generated automatically from [the
specification](portable-simd.md) using [the WebAssembly
mapping](webassembly-mapping.md).


## `b8x16` operations
| WebAssembly                                                  | Portable SIMD |
|:-------------------------------------------------------------|:--------------|
| `b8x16.build(x: i32[16]) -> b8x16`                           | [b8x16.build](portable-simd.md#build-vector-from-individual-lanes) |
| `b8x16.splat(x: i32) -> b8x16`                               | [b8x16.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `b8x16.extractLane(a: b8x16, i: LaneIdx16) -> i32`           | [b8x16.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `b8x16.replaceLane(a: b8x16, i: LaneIdx16, x: i32) -> b8x16` | [b8x16.replaceLane](portable-simd.md#replace-lane-value) |
| `b8x16.and(a: b8x16, b: b8x16) -> b8x16`                     | [b8x16.and](portable-simd.md#logical-and) |
| `b8x16.or(a: b8x16, b: b8x16) -> b8x16`                      | [b8x16.or](portable-simd.md#logical-or) |
| `b8x16.xor(a: b8x16, b: b8x16) -> b8x16`                     | [b8x16.xor](portable-simd.md#logical-xor) |
| `b8x16.not(a: b8x16) -> b8x16`                               | [b8x16.not](portable-simd.md#logical-not) |
| `b8x16.anyTrue(a: b8x16) -> i32`                             | [b8x16.anyTrue](portable-simd.md#any-lane-true) |
| `b8x16.allTrue(a: b8x16) -> i32`                             | [b8x16.allTrue](portable-simd.md#all-lanes-true) |

## `b16x8` operations
| WebAssembly                                                 | Portable SIMD |
|:------------------------------------------------------------|:--------------|
| `b16x8.build(x: i32[8]) -> b16x8`                           | [b16x8.build](portable-simd.md#build-vector-from-individual-lanes) |
| `b16x8.splat(x: i32) -> b16x8`                              | [b16x8.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `b16x8.extractLane(a: b16x8, i: LaneIdx8) -> i32`           | [b16x8.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `b16x8.replaceLane(a: b16x8, i: LaneIdx8, x: i32) -> b16x8` | [b16x8.replaceLane](portable-simd.md#replace-lane-value) |
| `b16x8.and(a: b16x8, b: b16x8) -> b16x8`                    | [b16x8.and](portable-simd.md#logical-and) |
| `b16x8.or(a: b16x8, b: b16x8) -> b16x8`                     | [b16x8.or](portable-simd.md#logical-or) |
| `b16x8.xor(a: b16x8, b: b16x8) -> b16x8`                    | [b16x8.xor](portable-simd.md#logical-xor) |
| `b16x8.not(a: b16x8) -> b16x8`                              | [b16x8.not](portable-simd.md#logical-not) |
| `b16x8.anyTrue(a: b16x8) -> i32`                            | [b16x8.anyTrue](portable-simd.md#any-lane-true) |
| `b16x8.allTrue(a: b16x8) -> i32`                            | [b16x8.allTrue](portable-simd.md#all-lanes-true) |

## `b32x4` operations
| WebAssembly                                                 | Portable SIMD |
|:------------------------------------------------------------|:--------------|
| `b32x4.build(x: i32[4]) -> b32x4`                           | [b32x4.build](portable-simd.md#build-vector-from-individual-lanes) |
| `b32x4.splat(x: i32) -> b32x4`                              | [b32x4.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `b32x4.extractLane(a: b32x4, i: LaneIdx4) -> i32`           | [b32x4.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `b32x4.replaceLane(a: b32x4, i: LaneIdx4, x: i32) -> b32x4` | [b32x4.replaceLane](portable-simd.md#replace-lane-value) |
| `b32x4.and(a: b32x4, b: b32x4) -> b32x4`                    | [b32x4.and](portable-simd.md#logical-and) |
| `b32x4.or(a: b32x4, b: b32x4) -> b32x4`                     | [b32x4.or](portable-simd.md#logical-or) |
| `b32x4.xor(a: b32x4, b: b32x4) -> b32x4`                    | [b32x4.xor](portable-simd.md#logical-xor) |
| `b32x4.not(a: b32x4) -> b32x4`                              | [b32x4.not](portable-simd.md#logical-not) |
| `b32x4.anyTrue(a: b32x4) -> i32`                            | [b32x4.anyTrue](portable-simd.md#any-lane-true) |
| `b32x4.allTrue(a: b32x4) -> i32`                            | [b32x4.allTrue](portable-simd.md#all-lanes-true) |

## `b64x2` operations
| WebAssembly                                                 | Portable SIMD |
|:------------------------------------------------------------|:--------------|
| `b64x2.build(x: i32[2]) -> b64x2`                           | [b64x2.build](portable-simd.md#build-vector-from-individual-lanes) |
| `b64x2.splat(x: i32) -> b64x2`                              | [b64x2.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `b64x2.extractLane(a: b64x2, i: LaneIdx2) -> i32`           | [b64x2.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `b64x2.replaceLane(a: b64x2, i: LaneIdx2, x: i32) -> b64x2` | [b64x2.replaceLane](portable-simd.md#replace-lane-value) |
| `b64x2.and(a: b64x2, b: b64x2) -> b64x2`                    | [b64x2.and](portable-simd.md#logical-and) |
| `b64x2.or(a: b64x2, b: b64x2) -> b64x2`                     | [b64x2.or](portable-simd.md#logical-or) |
| `b64x2.xor(a: b64x2, b: b64x2) -> b64x2`                    | [b64x2.xor](portable-simd.md#logical-xor) |
| `b64x2.not(a: b64x2) -> b64x2`                              | [b64x2.not](portable-simd.md#logical-not) |
| `b64x2.anyTrue(a: b64x2) -> i32`                            | [b64x2.anyTrue](portable-simd.md#any-lane-true) |
| `b64x2.allTrue(a: b64x2) -> i32`                            | [b64x2.allTrue](portable-simd.md#all-lanes-true) |

## `i8x16` operations
| WebAssembly                                                    | Portable SIMD |
|:---------------------------------------------------------------|:--------------|
| `i8x16.reinterpret/i16x8(a: i16x8) -> i8x16`                   | - |
| `i8x16.reinterpret/i32x4(a: i32x4) -> i8x16`                   | - |
| `i8x16.reinterpret/i64x2(a: i64x2) -> i8x16`                   | - |
| `i8x16.reinterpret/f32x4(a: f32x4) -> i8x16`                   | - |
| `i8x16.reinterpret/f64x2(a: f64x2) -> i8x16`                   | - |
| `i8x16.build(x: i32[16]) -> i8x16`                             | [i8x16.build](portable-simd.md#build-vector-from-individual-lanes) |
| `i8x16.splat(x: i32) -> i8x16`                                 | [i8x16.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `i8x16.extractLane_s(a: i8x16, i: LaneIdx16) -> i32`           | [i8x16.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i8x16.extractLane_u(a: i8x16, i: LaneIdx16) -> i32`           | [i8x16.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i8x16.replaceLane(a: i8x16, i: LaneIdx16, x: i32) -> i8x16`   | [i8x16.replaceLane](portable-simd.md#replace-lane-value) |
| `i8x16.select(s: b8x16, t: i8x16, f: i8x16) -> i8x16`          | [v8x16.select](portable-simd.md#lane-wise-select) |
| `i8x16.swizzle(a: i8x16, s: LaneIdx16[16]) -> i8x16`           | [v8x16.swizzle](portable-simd.md#swizzle-lanes) |
| `i8x16.shuffle(a: i8x16, b: i8x16, s: LaneIdx32[16]) -> i8x16` | [v8x16.shuffle](portable-simd.md#shuffle-lanes) |
| `i8x16.add(a: i8x16, b: i8x16) -> i8x16`                       | [i8x16.add](portable-simd.md#integer-addition) |
| `i8x16.sub(a: i8x16, b: i8x16) -> i8x16`                       | [i8x16.sub](portable-simd.md#integer-subtraction) |
| `i8x16.mul(a: i8x16, b: i8x16) -> i8x16`                       | [i8x16.mul](portable-simd.md#integer-multiplication) |
| `i8x16.neg(a: i8x16) -> i8x16`                                 | [i8x16.neg](portable-simd.md#integer-negation) |
| `i8x16.addSaturate_s(a: i8x16, b: i8x16) -> i8x16`             | [s8x16.addSaturate](portable-simd.md#saturating-integer-addition) |
| `i8x16.addSaturate_u(a: i8x16, b: i8x16) -> i8x16`             | [u8x16.addSaturate](portable-simd.md#saturating-integer-addition) |
| `i8x16.subSaturate_s(a: i8x16, b: i8x16) -> i8x16`             | [s8x16.subSaturate](portable-simd.md#saturating-integer-subtraction) |
| `i8x16.subSaturate_u(a: i8x16, b: i8x16) -> i8x16`             | [u8x16.subSaturate](portable-simd.md#saturating-integer-subtraction) |
| `i8x16.shl(a: i8x16, y: i32) -> i8x16`                         | [i8x16.shiftLeftByScalar](portable-simd.md#left-shift-by-scalar) |
| `i8x16.shr_s(a: i8x16, y: i32) -> i8x16`                       | [s8x16.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i8x16.shr_u(a: i8x16, y: i32) -> i8x16`                       | [u8x16.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i8x16.and(a: i8x16, b: i8x16) -> i8x16`                       | [v128.and](portable-simd.md#bitwise-operations) |
| `i8x16.or(a: i8x16, b: i8x16) -> i8x16`                        | [v128.or](portable-simd.md#bitwise-operations) |
| `i8x16.xor(a: i8x16, b: i8x16) -> i8x16`                       | [v128.xor](portable-simd.md#bitwise-operations) |
| `i8x16.not(a: i8x16) -> i8x16`                                 | [v128.not](portable-simd.md#bitwise-operations) |
| `i8x16.eq(a: i8x16, b: i8x16) -> b8x16`                        | [i8x16.equal](portable-simd.md#equality) |
| `i8x16.ne(a: i8x16, b: i8x16) -> b8x16`                        | [i8x16.notEqual](portable-simd.md#non-equality) |
| `i8x16.lt_s(a: i8x16, b: i8x16) -> b8x16`                      | [s8x16.lessThan](portable-simd.md#less-than) |
| `i8x16.lt_u(a: i8x16, b: i8x16) -> b8x16`                      | [u8x16.lessThan](portable-simd.md#less-than) |
| `i8x16.le_s(a: i8x16, b: i8x16) -> b8x16`                      | [s8x16.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i8x16.le_u(a: i8x16, b: i8x16) -> b8x16`                      | [u8x16.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i8x16.gt_s(a: i8x16, b: i8x16) -> b8x16`                      | [s8x16.greaterThan](portable-simd.md#greater-than) |
| `i8x16.gt_u(a: i8x16, b: i8x16) -> b8x16`                      | [u8x16.greaterThan](portable-simd.md#greater-than) |
| `i8x16.ge_s(a: i8x16, b: i8x16) -> b8x16`                      | [s8x16.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i8x16.ge_u(a: i8x16, b: i8x16) -> b8x16`                      | [u8x16.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i8x16.load(mem: Buffer, addr: ByteOffset) -> i8x16`           | [v8x16.load](portable-simd.md#load) |
| `i8x16.store(mem: Buffer, addr: ByteOffset, data: i8x16)`      | [v8x16.store](portable-simd.md#store) |

## `i16x8` operations
| WebAssembly                                                   | Portable SIMD |
|:--------------------------------------------------------------|:--------------|
| `i16x8.reinterpret/i8x16(a: i8x16) -> i16x8`                  | - |
| `i16x8.reinterpret/i32x4(a: i32x4) -> i16x8`                  | - |
| `i16x8.reinterpret/i64x2(a: i64x2) -> i16x8`                  | - |
| `i16x8.reinterpret/f32x4(a: f32x4) -> i16x8`                  | - |
| `i16x8.reinterpret/f64x2(a: f64x2) -> i16x8`                  | - |
| `i16x8.build(x: i32[8]) -> i16x8`                             | [i16x8.build](portable-simd.md#build-vector-from-individual-lanes) |
| `i16x8.splat(x: i32) -> i16x8`                                | [i16x8.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `i16x8.extractLane_s(a: i16x8, i: LaneIdx8) -> i32`           | [i16x8.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i16x8.extractLane_u(a: i16x8, i: LaneIdx8) -> i32`           | [i16x8.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i16x8.replaceLane(a: i16x8, i: LaneIdx8, x: i32) -> i16x8`   | [i16x8.replaceLane](portable-simd.md#replace-lane-value) |
| `i16x8.select(s: b16x8, t: i16x8, f: i16x8) -> i16x8`         | [v16x8.select](portable-simd.md#lane-wise-select) |
| `i16x8.swizzle(a: i16x8, s: LaneIdx8[8]) -> i16x8`            | [v16x8.swizzle](portable-simd.md#swizzle-lanes) |
| `i16x8.shuffle(a: i16x8, b: i16x8, s: LaneIdx16[8]) -> i16x8` | [v16x8.shuffle](portable-simd.md#shuffle-lanes) |
| `i16x8.add(a: i16x8, b: i16x8) -> i16x8`                      | [i16x8.add](portable-simd.md#integer-addition) |
| `i16x8.sub(a: i16x8, b: i16x8) -> i16x8`                      | [i16x8.sub](portable-simd.md#integer-subtraction) |
| `i16x8.mul(a: i16x8, b: i16x8) -> i16x8`                      | [i16x8.mul](portable-simd.md#integer-multiplication) |
| `i16x8.neg(a: i16x8) -> i16x8`                                | [i16x8.neg](portable-simd.md#integer-negation) |
| `i16x8.addSaturate_s(a: i16x8, b: i16x8) -> i16x8`            | [s16x8.addSaturate](portable-simd.md#saturating-integer-addition) |
| `i16x8.addSaturate_u(a: i16x8, b: i16x8) -> i16x8`            | [u16x8.addSaturate](portable-simd.md#saturating-integer-addition) |
| `i16x8.subSaturate_s(a: i16x8, b: i16x8) -> i16x8`            | [s16x8.subSaturate](portable-simd.md#saturating-integer-subtraction) |
| `i16x8.subSaturate_u(a: i16x8, b: i16x8) -> i16x8`            | [u16x8.subSaturate](portable-simd.md#saturating-integer-subtraction) |
| `i16x8.shl(a: i16x8, y: i32) -> i16x8`                        | [i16x8.shiftLeftByScalar](portable-simd.md#left-shift-by-scalar) |
| `i16x8.shr_s(a: i16x8, y: i32) -> i16x8`                      | [s16x8.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i16x8.shr_u(a: i16x8, y: i32) -> i16x8`                      | [u16x8.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i16x8.and(a: i16x8, b: i16x8) -> i16x8`                      | [v128.and](portable-simd.md#bitwise-operations) |
| `i16x8.or(a: i16x8, b: i16x8) -> i16x8`                       | [v128.or](portable-simd.md#bitwise-operations) |
| `i16x8.xor(a: i16x8, b: i16x8) -> i16x8`                      | [v128.xor](portable-simd.md#bitwise-operations) |
| `i16x8.not(a: i16x8) -> i16x8`                                | [v128.not](portable-simd.md#bitwise-operations) |
| `i16x8.eq(a: i16x8, b: i16x8) -> b16x8`                       | [i16x8.equal](portable-simd.md#equality) |
| `i16x8.ne(a: i16x8, b: i16x8) -> b16x8`                       | [i16x8.notEqual](portable-simd.md#non-equality) |
| `i16x8.lt_s(a: i16x8, b: i16x8) -> b16x8`                     | [s16x8.lessThan](portable-simd.md#less-than) |
| `i16x8.lt_u(a: i16x8, b: i16x8) -> b16x8`                     | [u16x8.lessThan](portable-simd.md#less-than) |
| `i16x8.le_s(a: i16x8, b: i16x8) -> b16x8`                     | [s16x8.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i16x8.le_u(a: i16x8, b: i16x8) -> b16x8`                     | [u16x8.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i16x8.gt_s(a: i16x8, b: i16x8) -> b16x8`                     | [s16x8.greaterThan](portable-simd.md#greater-than) |
| `i16x8.gt_u(a: i16x8, b: i16x8) -> b16x8`                     | [u16x8.greaterThan](portable-simd.md#greater-than) |
| `i16x8.ge_s(a: i16x8, b: i16x8) -> b16x8`                     | [s16x8.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i16x8.ge_u(a: i16x8, b: i16x8) -> b16x8`                     | [u16x8.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i16x8.load(mem: Buffer, addr: ByteOffset) -> i16x8`          | [v16x8.load](portable-simd.md#load) |
| `i16x8.store(mem: Buffer, addr: ByteOffset, data: i16x8)`     | [v16x8.store](portable-simd.md#store) |

## `i32x4` operations
| WebAssembly                                                      | Portable SIMD |
|:-----------------------------------------------------------------|:--------------|
| `i32x4.reinterpret/i8x16(a: i8x16) -> i32x4`                     | - |
| `i32x4.reinterpret/i16x8(a: i16x8) -> i32x4`                     | - |
| `i32x4.reinterpret/i64x2(a: i64x2) -> i32x4`                     | - |
| `i32x4.reinterpret/f32x4(a: f32x4) -> i32x4`                     | - |
| `i32x4.reinterpret/f64x2(a: f64x2) -> i32x4`                     | - |
| `i32x4.build(x: i32[4]) -> i32x4`                                | [i32x4.build](portable-simd.md#build-vector-from-individual-lanes) |
| `i32x4.splat(x: i32) -> i32x4`                                   | [i32x4.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `i32x4.extractLane(a: i32x4, i: LaneIdx4) -> i32`                | [i32x4.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i32x4.replaceLane(a: i32x4, i: LaneIdx4, x: i32) -> i32x4`      | [i32x4.replaceLane](portable-simd.md#replace-lane-value) |
| `i32x4.select(s: b32x4, t: i32x4, f: i32x4) -> i32x4`            | [v32x4.select](portable-simd.md#lane-wise-select) |
| `i32x4.swizzle(a: i32x4, s: LaneIdx4[4]) -> i32x4`               | [v32x4.swizzle](portable-simd.md#swizzle-lanes) |
| `i32x4.shuffle(a: i32x4, b: i32x4, s: LaneIdx8[4]) -> i32x4`     | [v32x4.shuffle](portable-simd.md#shuffle-lanes) |
| `i32x4.add(a: i32x4, b: i32x4) -> i32x4`                         | [i32x4.add](portable-simd.md#integer-addition) |
| `i32x4.sub(a: i32x4, b: i32x4) -> i32x4`                         | [i32x4.sub](portable-simd.md#integer-subtraction) |
| `i32x4.mul(a: i32x4, b: i32x4) -> i32x4`                         | [i32x4.mul](portable-simd.md#integer-multiplication) |
| `i32x4.neg(a: i32x4) -> i32x4`                                   | [i32x4.neg](portable-simd.md#integer-negation) |
| `i32x4.shl(a: i32x4, y: i32) -> i32x4`                           | [i32x4.shiftLeftByScalar](portable-simd.md#left-shift-by-scalar) |
| `i32x4.shr_s(a: i32x4, y: i32) -> i32x4`                         | [s32x4.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i32x4.shr_u(a: i32x4, y: i32) -> i32x4`                         | [u32x4.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i32x4.and(a: i32x4, b: i32x4) -> i32x4`                         | [v128.and](portable-simd.md#bitwise-operations) |
| `i32x4.or(a: i32x4, b: i32x4) -> i32x4`                          | [v128.or](portable-simd.md#bitwise-operations) |
| `i32x4.xor(a: i32x4, b: i32x4) -> i32x4`                         | [v128.xor](portable-simd.md#bitwise-operations) |
| `i32x4.not(a: i32x4) -> i32x4`                                   | [v128.not](portable-simd.md#bitwise-operations) |
| `i32x4.eq(a: i32x4, b: i32x4) -> b32x4`                          | [i32x4.equal](portable-simd.md#equality) |
| `i32x4.ne(a: i32x4, b: i32x4) -> b32x4`                          | [i32x4.notEqual](portable-simd.md#non-equality) |
| `i32x4.lt_s(a: i32x4, b: i32x4) -> b32x4`                        | [s32x4.lessThan](portable-simd.md#less-than) |
| `i32x4.lt_u(a: i32x4, b: i32x4) -> b32x4`                        | [u32x4.lessThan](portable-simd.md#less-than) |
| `i32x4.le_s(a: i32x4, b: i32x4) -> b32x4`                        | [s32x4.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i32x4.le_u(a: i32x4, b: i32x4) -> b32x4`                        | [u32x4.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i32x4.gt_s(a: i32x4, b: i32x4) -> b32x4`                        | [s32x4.greaterThan](portable-simd.md#greater-than) |
| `i32x4.gt_u(a: i32x4, b: i32x4) -> b32x4`                        | [u32x4.greaterThan](portable-simd.md#greater-than) |
| `i32x4.ge_s(a: i32x4, b: i32x4) -> b32x4`                        | [s32x4.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i32x4.ge_u(a: i32x4, b: i32x4) -> b32x4`                        | [u32x4.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i32x4.load(mem: Buffer, addr: ByteOffset) -> i32x4`             | [v32x4.load](portable-simd.md#load) |
| `i32x4.store(mem: Buffer, addr: ByteOffset, data: i32x4)`        | [v32x4.store](portable-simd.md#store) |
| `i32x4.load1(mem: Buffer, addr: ByteOffset) -> i32x4`            | [v32x4.load1](portable-simd.md#partial-load) |
| `i32x4.load2(mem: Buffer, addr: ByteOffset) -> i32x4`            | [v32x4.load2](portable-simd.md#partial-load) |
| `i32x4.load3(mem: Buffer, addr: ByteOffset) -> i32x4`            | [v32x4.load3](portable-simd.md#partial-load) |
| `i32x4.store1(mem: Buffer, addr: ByteOffset, data: i32x4)`       | [v32x4.store1](portable-simd.md#partial-store) |
| `i32x4.store2(mem: Buffer, addr: ByteOffset, data: i32x4)`       | [v32x4.store2](portable-simd.md#partial-store) |
| `i32x4.store3(mem: Buffer, addr: ByteOffset, data: i32x4)`       | [v32x4.store3](portable-simd.md#partial-store) |
| `i32x4.trunc_s(a: f32x4) -> (result: f32x4, fail: i32) -> i32x4` | [s32x4.fromFloat](portable-simd.md#floating-point-to-integer) |
| `i32x4.trunc_u(a: f32x4) -> (result: f32x4, fail: i32) -> i32x4` | [u32x4.fromFloat](portable-simd.md#floating-point-to-integer) |

## `i64x2` operations
| WebAssembly                                                      | Portable SIMD |
|:-----------------------------------------------------------------|:--------------|
| `i64x2.reinterpret/i8x16(a: i8x16) -> i64x2`                     | - |
| `i64x2.reinterpret/i16x8(a: i16x8) -> i64x2`                     | - |
| `i64x2.reinterpret/i32x4(a: i32x4) -> i64x2`                     | - |
| `i64x2.reinterpret/f32x4(a: f32x4) -> i64x2`                     | - |
| `i64x2.reinterpret/f64x2(a: f64x2) -> i64x2`                     | - |
| `i64x2.build(x: i64[2]) -> i64x2`                                | [i64x2.build](portable-simd.md#build-vector-from-individual-lanes) |
| `i64x2.splat(x: i64) -> i64x2`                                   | [i64x2.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `i64x2.extractLane(a: i64x2, i: LaneIdx2) -> i64`                | [i64x2.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `i64x2.replaceLane(a: i64x2, i: LaneIdx2, x: i64) -> i64x2`      | [i64x2.replaceLane](portable-simd.md#replace-lane-value) |
| `i64x2.select(s: b64x2, t: i64x2, f: i64x2) -> i64x2`            | [v64x2.select](portable-simd.md#lane-wise-select) |
| `i64x2.swizzle(a: i64x2, s: LaneIdx2[2]) -> i64x2`               | [v64x2.swizzle](portable-simd.md#swizzle-lanes) |
| `i64x2.shuffle(a: i64x2, b: i64x2, s: LaneIdx4[2]) -> i64x2`     | [v64x2.shuffle](portable-simd.md#shuffle-lanes) |
| `i64x2.add(a: i64x2, b: i64x2) -> i64x2`                         | [i64x2.add](portable-simd.md#integer-addition) |
| `i64x2.sub(a: i64x2, b: i64x2) -> i64x2`                         | [i64x2.sub](portable-simd.md#integer-subtraction) |
| `i64x2.mul(a: i64x2, b: i64x2) -> i64x2`                         | [i64x2.mul](portable-simd.md#integer-multiplication) |
| `i64x2.neg(a: i64x2) -> i64x2`                                   | [i64x2.neg](portable-simd.md#integer-negation) |
| `i64x2.shl(a: i64x2, y: i32) -> i64x2`                           | [i64x2.shiftLeftByScalar](portable-simd.md#left-shift-by-scalar) |
| `i64x2.shr_s(a: i64x2, y: i32) -> i64x2`                         | [s64x2.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i64x2.shr_u(a: i64x2, y: i32) -> i64x2`                         | [u64x2.shiftRightByScalar](portable-simd.md#right-shift-by-scalar) |
| `i64x2.and(a: i64x2, b: i64x2) -> i64x2`                         | [v128.and](portable-simd.md#bitwise-operations) |
| `i64x2.or(a: i64x2, b: i64x2) -> i64x2`                          | [v128.or](portable-simd.md#bitwise-operations) |
| `i64x2.xor(a: i64x2, b: i64x2) -> i64x2`                         | [v128.xor](portable-simd.md#bitwise-operations) |
| `i64x2.not(a: i64x2) -> i64x2`                                   | [v128.not](portable-simd.md#bitwise-operations) |
| `i64x2.eq(a: i64x2, b: i64x2) -> b64x2`                          | [i64x2.equal](portable-simd.md#equality) |
| `i64x2.ne(a: i64x2, b: i64x2) -> b64x2`                          | [i64x2.notEqual](portable-simd.md#non-equality) |
| `i64x2.lt_s(a: i64x2, b: i64x2) -> b64x2`                        | [s64x2.lessThan](portable-simd.md#less-than) |
| `i64x2.lt_u(a: i64x2, b: i64x2) -> b64x2`                        | [u64x2.lessThan](portable-simd.md#less-than) |
| `i64x2.le_s(a: i64x2, b: i64x2) -> b64x2`                        | [s64x2.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i64x2.le_u(a: i64x2, b: i64x2) -> b64x2`                        | [u64x2.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `i64x2.gt_s(a: i64x2, b: i64x2) -> b64x2`                        | [s64x2.greaterThan](portable-simd.md#greater-than) |
| `i64x2.gt_u(a: i64x2, b: i64x2) -> b64x2`                        | [u64x2.greaterThan](portable-simd.md#greater-than) |
| `i64x2.ge_s(a: i64x2, b: i64x2) -> b64x2`                        | [s64x2.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i64x2.ge_u(a: i64x2, b: i64x2) -> b64x2`                        | [u64x2.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `i64x2.load(mem: Buffer, addr: ByteOffset) -> i64x2`             | [v64x2.load](portable-simd.md#load) |
| `i64x2.store(mem: Buffer, addr: ByteOffset, data: i64x2)`        | [v64x2.store](portable-simd.md#store) |
| `i64x2.trunc_s(a: f64x2) -> (result: f64x2, fail: i32) -> i64x2` | [s64x2.fromFloat](portable-simd.md#floating-point-to-integer) |
| `i64x2.trunc_u(a: f64x2) -> (result: f64x2, fail: i32) -> i64x2` | [u64x2.fromFloat](portable-simd.md#floating-point-to-integer) |

## `f32x4` operations
| WebAssembly                                                   | Portable SIMD |
|:--------------------------------------------------------------|:--------------|
| `f32x4.reinterpret/i8x16(a: i8x16) -> f32x4`                  | - |
| `f32x4.reinterpret/i16x8(a: i16x8) -> f32x4`                  | - |
| `f32x4.reinterpret/i32x4(a: i32x4) -> f32x4`                  | - |
| `f32x4.reinterpret/i64x2(a: i64x2) -> f32x4`                  | - |
| `f32x4.reinterpret/f64x2(a: f64x2) -> f32x4`                  | - |
| `f32x4.build(x: f32[4]) -> f32x4`                             | [f32x4.build](portable-simd.md#build-vector-from-individual-lanes) |
| `f32x4.splat(x: f32) -> f32x4`                                | [f32x4.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `f32x4.extractLane(a: f32x4, i: LaneIdx4) -> f32`             | [f32x4.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `f32x4.replaceLane(a: f32x4, i: LaneIdx4, x: f32) -> f32x4`   | [f32x4.replaceLane](portable-simd.md#replace-lane-value) |
| `f32x4.select(s: b32x4, t: f32x4, f: f32x4) -> f32x4`         | [v32x4.select](portable-simd.md#lane-wise-select) |
| `f32x4.swizzle(a: f32x4, s: LaneIdx4[4]) -> f32x4`            | [v32x4.swizzle](portable-simd.md#swizzle-lanes) |
| `f32x4.shuffle(a: f32x4, b: f32x4, s: LaneIdx8[4]) -> f32x4`  | [v32x4.shuffle](portable-simd.md#shuffle-lanes) |
| `f32x4.add(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | [f32x4.add](portable-simd.md#addition) |
| `f32x4.sub(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | [f32x4.sub](portable-simd.md#subtraction) |
| `f32x4.mul(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | [f32x4.mul](portable-simd.md#multiplication) |
| `f32x4.neg(a: f32x4) -> f32x4`                                | [f32x4.neg](portable-simd.md#negation) |
| `f32x4.and(a: f32x4, b: f32x4) -> f32x4`                      | [v128.and](portable-simd.md#bitwise-operations) |
| `f32x4.or(a: f32x4, b: f32x4) -> f32x4`                       | [v128.or](portable-simd.md#bitwise-operations) |
| `f32x4.xor(a: f32x4, b: f32x4) -> f32x4`                      | [v128.xor](portable-simd.md#bitwise-operations) |
| `f32x4.not(a: f32x4) -> f32x4`                                | [v128.not](portable-simd.md#bitwise-operations) |
| `f32x4.eq(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.equal](portable-simd.md#equality) |
| `f32x4.ne(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.notEqual](portable-simd.md#non-equality) |
| `f32x4.lt(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.lessThan](portable-simd.md#less-than) |
| `f32x4.le(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `f32x4.gt(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.greaterThan](portable-simd.md#greater-than) |
| `f32x4.ge(a: f32x4, b: f32x4) -> b32x4`                       | [f32x4.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `f32x4.load(mem: Buffer, addr: ByteOffset) -> f32x4`          | [v32x4.load](portable-simd.md#load) |
| `f32x4.store(mem: Buffer, addr: ByteOffset, data: f32x4)`     | [v32x4.store](portable-simd.md#store) |
| `f32x4.load1(mem: Buffer, addr: ByteOffset) -> f32x4`         | [v32x4.load1](portable-simd.md#partial-load) |
| `f32x4.load2(mem: Buffer, addr: ByteOffset) -> f32x4`         | [v32x4.load2](portable-simd.md#partial-load) |
| `f32x4.load3(mem: Buffer, addr: ByteOffset) -> f32x4`         | [v32x4.load3](portable-simd.md#partial-load) |
| `f32x4.store1(mem: Buffer, addr: ByteOffset, data: f32x4)`    | [v32x4.store1](portable-simd.md#partial-store) |
| `f32x4.store2(mem: Buffer, addr: ByteOffset, data: f32x4)`    | [v32x4.store2](portable-simd.md#partial-store) |
| `f32x4.store3(mem: Buffer, addr: ByteOffset, data: f32x4)`    | [v32x4.store3](portable-simd.md#partial-store) |
| `f32x4.abs(a: f32x4) -> f32x4`                                | [f32x4.abs](portable-simd.md#absolute-value) |
| `f32x4.min(a: f32x4, b: f32x4) -> f32x4`                      | [f32x4.min](portable-simd.md#nan-propagating-minimum) |
| `f32x4.max(a: f32x4, b: f32x4) -> f32x4`                      | [f32x4.max](portable-simd.md#nan-propagating-maximum) |
| `f32x4.minNum(a: f32x4, b: f32x4) -> f32x4`                   | [f32x4.minNum](portable-simd.md#nan-suppressing-minimum) |
| `f32x4.maxNum(a: f32x4, b: f32x4) -> f32x4`                   | [f32x4.maxNum](portable-simd.md#nan-suppressing-maximum) |
| `f32x4.div(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | [f32x4.div](portable-simd.md#division) |
| `f32x4.sqrt(a: f32x4, rmode: RoundingMode) -> f32x4`          | [f32x4.sqrt](portable-simd.md#square-root) |
| `f32x4.reciprocalApproximation(a: f32x4) -> f32x4`            | [f32x4.reciprocalApproximation](portable-simd.md#reciprocal-approximation) |
| `f32x4.reciprocalSqrtApproximation(a: f32x4) -> f32x4`        | [f32x4.reciprocalSqrtApproximation](portable-simd.md#reciprocal-square-root-approximation) |
| `f32x4.convert_s(a: i32x4, rmode: RoundingMode) -> f32x4`     | [f32x4.fromSignedInt](portable-simd.md#integer-to-floating-point) |
| `f32x4.convert_u(a: i32x4, rmode: RoundingMode) -> f32x4`     | [f32x4.fromUnsignedInt](portable-simd.md#integer-to-floating-point) |

## `f64x2` operations
| WebAssembly                                                   | Portable SIMD |
|:--------------------------------------------------------------|:--------------|
| `f64x2.reinterpret/i8x16(a: i8x16) -> f64x2`                  | - |
| `f64x2.reinterpret/i16x8(a: i16x8) -> f64x2`                  | - |
| `f64x2.reinterpret/i32x4(a: i32x4) -> f64x2`                  | - |
| `f64x2.reinterpret/i64x2(a: i64x2) -> f64x2`                  | - |
| `f64x2.reinterpret/f32x4(a: f32x4) -> f64x2`                  | - |
| `f64x2.build(x: f64[2]) -> f64x2`                             | [f64x2.build](portable-simd.md#build-vector-from-individual-lanes) |
| `f64x2.splat(x: f64) -> f64x2`                                | [f64x2.splat](portable-simd.md#create-vector-with-identical-lanes) |
| `f64x2.extractLane(a: f64x2, i: LaneIdx2) -> f64`             | [f64x2.extractLane](portable-simd.md#extract-lane-as-a-scalar) |
| `f64x2.replaceLane(a: f64x2, i: LaneIdx2, x: f64) -> f64x2`   | [f64x2.replaceLane](portable-simd.md#replace-lane-value) |
| `f64x2.select(s: b64x2, t: f64x2, f: f64x2) -> f64x2`         | [v64x2.select](portable-simd.md#lane-wise-select) |
| `f64x2.swizzle(a: f64x2, s: LaneIdx2[2]) -> f64x2`            | [v64x2.swizzle](portable-simd.md#swizzle-lanes) |
| `f64x2.shuffle(a: f64x2, b: f64x2, s: LaneIdx4[2]) -> f64x2`  | [v64x2.shuffle](portable-simd.md#shuffle-lanes) |
| `f64x2.add(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | [f64x2.add](portable-simd.md#addition) |
| `f64x2.sub(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | [f64x2.sub](portable-simd.md#subtraction) |
| `f64x2.mul(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | [f64x2.mul](portable-simd.md#multiplication) |
| `f64x2.neg(a: f64x2) -> f64x2`                                | [f64x2.neg](portable-simd.md#negation) |
| `f64x2.and(a: f64x2, b: f64x2) -> f64x2`                      | [v128.and](portable-simd.md#bitwise-operations) |
| `f64x2.or(a: f64x2, b: f64x2) -> f64x2`                       | [v128.or](portable-simd.md#bitwise-operations) |
| `f64x2.xor(a: f64x2, b: f64x2) -> f64x2`                      | [v128.xor](portable-simd.md#bitwise-operations) |
| `f64x2.not(a: f64x2) -> f64x2`                                | [v128.not](portable-simd.md#bitwise-operations) |
| `f64x2.eq(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.equal](portable-simd.md#equality) |
| `f64x2.ne(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.notEqual](portable-simd.md#non-equality) |
| `f64x2.lt(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.lessThan](portable-simd.md#less-than) |
| `f64x2.le(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.lessThanOrEqual](portable-simd.md#less-than-or-equal) |
| `f64x2.gt(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.greaterThan](portable-simd.md#greater-than) |
| `f64x2.ge(a: f64x2, b: f64x2) -> b64x2`                       | [f64x2.greaterThanOrEqual](portable-simd.md#greater-than-or-equal) |
| `f64x2.load(mem: Buffer, addr: ByteOffset) -> f64x2`          | [v64x2.load](portable-simd.md#load) |
| `f64x2.store(mem: Buffer, addr: ByteOffset, data: f64x2)`     | [v64x2.store](portable-simd.md#store) |
| `f64x2.abs(a: f64x2) -> f64x2`                                | [f64x2.abs](portable-simd.md#absolute-value) |
| `f64x2.min(a: f64x2, b: f64x2) -> f64x2`                      | [f64x2.min](portable-simd.md#nan-propagating-minimum) |
| `f64x2.max(a: f64x2, b: f64x2) -> f64x2`                      | [f64x2.max](portable-simd.md#nan-propagating-maximum) |
| `f64x2.minNum(a: f64x2, b: f64x2) -> f64x2`                   | [f64x2.minNum](portable-simd.md#nan-suppressing-minimum) |
| `f64x2.maxNum(a: f64x2, b: f64x2) -> f64x2`                   | [f64x2.maxNum](portable-simd.md#nan-suppressing-maximum) |
| `f64x2.div(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | [f64x2.div](portable-simd.md#division) |
| `f64x2.sqrt(a: f64x2, rmode: RoundingMode) -> f64x2`          | [f64x2.sqrt](portable-simd.md#square-root) |
| `f64x2.reciprocalApproximation(a: f64x2) -> f64x2`            | [f64x2.reciprocalApproximation](portable-simd.md#reciprocal-approximation) |
| `f64x2.reciprocalSqrtApproximation(a: f64x2) -> f64x2`        | [f64x2.reciprocalSqrtApproximation](portable-simd.md#reciprocal-square-root-approximation) |
| `f64x2.convert_s(a: i64x2, rmode: RoundingMode) -> f64x2`     | [f64x2.fromSignedInt](portable-simd.md#integer-to-floating-point) |
| `f64x2.convert_u(a: i64x2, rmode: RoundingMode) -> f64x2`     | [f64x2.fromUnsignedInt](portable-simd.md#integer-to-floating-point) |
