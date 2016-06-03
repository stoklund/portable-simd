
# WebAssembly SIMD operations

This table is generated automatically from [the
specification](portable-simd.md) using [the WebAssembly
mapping](webassembly-mapping.md).


## `b8x16` operations
| WebAssembly                                                      | Portable SIMD       |
|:-----------------------------------------------------------------|:--------------------|
| `b8x16.build(x: boolean[16]) -> b8x16`                           | `b8x16.build`       |
| `b8x16.splat(x: boolean) -> b8x16`                               | `b8x16.splat`       |
| `b8x16.extractLane(a: b8x16, i: LaneIdx16) -> boolean`           | `b8x16.extractLane` |
| `b8x16.replaceLane(a: b8x16, i: LaneIdx16, x: boolean) -> b8x16` | `b8x16.replaceLane` |
| `b8x16.and(a: b8x16, b: b8x16) -> b8x16`                         | `b8x16.and`         |
| `b8x16.or(a: b8x16, b: b8x16) -> b8x16`                          | `b8x16.or`          |
| `b8x16.xor(a: b8x16, b: b8x16) -> b8x16`                         | `b8x16.xor`         |
| `b8x16.not(a: b8x16) -> b8x16`                                   | `b8x16.not`         |
| `b8x16.anyTrue(a: b8x16) -> boolean`                             | `b8x16.anyTrue`     |
| `b8x16.allTrue(a: b8x16) -> boolean`                             | `b8x16.allTrue`     |

## `b16x8` operations
| WebAssembly                                                     | Portable SIMD       |
|:----------------------------------------------------------------|:--------------------|
| `b16x8.build(x: boolean[8]) -> b16x8`                           | `b16x8.build`       |
| `b16x8.splat(x: boolean) -> b16x8`                              | `b16x8.splat`       |
| `b16x8.extractLane(a: b16x8, i: LaneIdx8) -> boolean`           | `b16x8.extractLane` |
| `b16x8.replaceLane(a: b16x8, i: LaneIdx8, x: boolean) -> b16x8` | `b16x8.replaceLane` |
| `b16x8.and(a: b16x8, b: b16x8) -> b16x8`                        | `b16x8.and`         |
| `b16x8.or(a: b16x8, b: b16x8) -> b16x8`                         | `b16x8.or`          |
| `b16x8.xor(a: b16x8, b: b16x8) -> b16x8`                        | `b16x8.xor`         |
| `b16x8.not(a: b16x8) -> b16x8`                                  | `b16x8.not`         |
| `b16x8.anyTrue(a: b16x8) -> boolean`                            | `b16x8.anyTrue`     |
| `b16x8.allTrue(a: b16x8) -> boolean`                            | `b16x8.allTrue`     |

## `b32x4` operations
| WebAssembly                                                     | Portable SIMD       |
|:----------------------------------------------------------------|:--------------------|
| `b32x4.build(x: boolean[4]) -> b32x4`                           | `b32x4.build`       |
| `b32x4.splat(x: boolean) -> b32x4`                              | `b32x4.splat`       |
| `b32x4.extractLane(a: b32x4, i: LaneIdx4) -> boolean`           | `b32x4.extractLane` |
| `b32x4.replaceLane(a: b32x4, i: LaneIdx4, x: boolean) -> b32x4` | `b32x4.replaceLane` |
| `b32x4.and(a: b32x4, b: b32x4) -> b32x4`                        | `b32x4.and`         |
| `b32x4.or(a: b32x4, b: b32x4) -> b32x4`                         | `b32x4.or`          |
| `b32x4.xor(a: b32x4, b: b32x4) -> b32x4`                        | `b32x4.xor`         |
| `b32x4.not(a: b32x4) -> b32x4`                                  | `b32x4.not`         |
| `b32x4.anyTrue(a: b32x4) -> boolean`                            | `b32x4.anyTrue`     |
| `b32x4.allTrue(a: b32x4) -> boolean`                            | `b32x4.allTrue`     |

## `b64x2` operations
| WebAssembly                                                     | Portable SIMD       |
|:----------------------------------------------------------------|:--------------------|
| `b64x2.build(x: boolean[2]) -> b64x2`                           | `b64x2.build`       |
| `b64x2.splat(x: boolean) -> b64x2`                              | `b64x2.splat`       |
| `b64x2.extractLane(a: b64x2, i: LaneIdx2) -> boolean`           | `b64x2.extractLane` |
| `b64x2.replaceLane(a: b64x2, i: LaneIdx2, x: boolean) -> b64x2` | `b64x2.replaceLane` |
| `b64x2.and(a: b64x2, b: b64x2) -> b64x2`                        | `b64x2.and`         |
| `b64x2.or(a: b64x2, b: b64x2) -> b64x2`                         | `b64x2.or`          |
| `b64x2.xor(a: b64x2, b: b64x2) -> b64x2`                        | `b64x2.xor`         |
| `b64x2.not(a: b64x2) -> b64x2`                                  | `b64x2.not`         |
| `b64x2.anyTrue(a: b64x2) -> boolean`                            | `b64x2.anyTrue`     |
| `b64x2.allTrue(a: b64x2) -> boolean`                            | `b64x2.allTrue`     |

## `i8x16` operations
| WebAssembly                                                    | Portable SIMD              |
|:---------------------------------------------------------------|:---------------------------|
| `i8x16.reinterpret/i16x8(a: i16x8) -> i8x16`                   | `-`                        |
| `i8x16.reinterpret/i32x4(a: i32x4) -> i8x16`                   | `-`                        |
| `i8x16.reinterpret/i64x2(a: i64x2) -> i8x16`                   | `-`                        |
| `i8x16.reinterpret/f32x4(a: f32x4) -> i8x16`                   | `-`                        |
| `i8x16.reinterpret/f64x2(a: f64x2) -> i8x16`                   | `-`                        |
| `i8x16.build(x: i8[16]) -> i8x16`                              | `i8x16.build`              |
| `i8x16.splat(x: i8) -> i8x16`                                  | `i8x16.splat`              |
| `i8x16.extractLane(a: i8x16, i: LaneIdx16) -> i8`              | `i8x16.extractLane`        |
| `i8x16.replaceLane(a: i8x16, i: LaneIdx16, x: i8) -> i8x16`    | `i8x16.replaceLane`        |
| `i8x16.select(s: b8x16, t: i8x16, f: i8x16) -> i8x16`          | `v8x16.select`             |
| `i8x16.swizzle(a: i8x16, s: LaneIdx16[16]) -> i8x16`           | `v8x16.swizzle`            |
| `i8x16.shuffle(a: i8x16, b: i8x16, s: LaneIdx32[16]) -> i8x16` | `v8x16.shuffle`            |
| `i8x16.add(a: i8x16, b: i8x16) -> i8x16`                       | `i8x16.add`                |
| `i8x16.sub(a: i8x16, b: i8x16) -> i8x16`                       | `i8x16.sub`                |
| `i8x16.mul(a: i8x16, b: i8x16) -> i8x16`                       | `i8x16.mul`                |
| `i8x16.neg(a: i8x16) -> i8x16`                                 | `i8x16.neg`                |
| `i8x16.addSaturate_s(a: i8x16, b: i8x16) -> i8x16`             | `s8x16.addSaturate`        |
| `i8x16.addSaturate_u(a: i8x16, b: i8x16) -> i8x16`             | `u8x16.addSaturate`        |
| `i8x16.subSaturate_s(a: i8x16, b: i8x16) -> i8x16`             | `s8x16.subSaturate`        |
| `i8x16.subSaturate_u(a: i8x16, b: i8x16) -> i8x16`             | `u8x16.subSaturate`        |
| `i8x16.shl(a: i8x16, y: i8) -> i8x16`                          | `i8x16.shiftLeftByScalar`  |
| `i8x16.shr_s(a: i8x16, y: i8) -> i8x16`                        | `s8x16.shiftRightByScalar` |
| `i8x16.shr_u(a: i8x16, y: i8) -> i8x16`                        | `u8x16.shiftRightByScalar` |
| `i8x16.and(a: i8x16, b: i8x16) -> i8x16`                       | `v128.and`                 |
| `i8x16.or(a: i8x16, b: i8x16) -> i8x16`                        | `v128.or`                  |
| `i8x16.xor(a: i8x16, b: i8x16) -> i8x16`                       | `v128.xor`                 |
| `i8x16.not(a: i8x16) -> i8x16`                                 | `v128.not`                 |
| `i8x16.eq(a: i8x16, b: i8x16) -> b8x16`                        | `i8x16.equal`              |
| `i8x16.ne(a: i8x16, b: i8x16) -> b8x16`                        | `i8x16.notEqual`           |
| `i8x16.lt_s(a: i8x16, b: i8x16) -> b8x16`                      | `s8x16.lessThan`           |
| `i8x16.lt_u(a: i8x16, b: i8x16) -> b8x16`                      | `u8x16.lessThan`           |
| `i8x16.le_s(a: i8x16, b: i8x16) -> b8x16`                      | `s8x16.lessThanOrEqual`    |
| `i8x16.le_u(a: i8x16, b: i8x16) -> b8x16`                      | `u8x16.lessThanOrEqual`    |
| `i8x16.gt_s(a: i8x16, b: i8x16) -> b8x16`                      | `s8x16.greaterThan`        |
| `i8x16.gt_u(a: i8x16, b: i8x16) -> b8x16`                      | `u8x16.greaterThan`        |
| `i8x16.ge_s(a: i8x16, b: i8x16) -> b8x16`                      | `s8x16.greaterThanOrEqual` |
| `i8x16.ge_u(a: i8x16, b: i8x16) -> b8x16`                      | `u8x16.greaterThanOrEqual` |
| `i8x16.load(mem: Buffer, addr: ByteOffset) -> i8x16`           | `v8x16.load`               |
| `i8x16.store(mem: Buffer, addr: ByteOffset, data: i8x16)`      | `v8x16.store`              |

## `i16x8` operations
| WebAssembly                                                   | Portable SIMD              |
|:--------------------------------------------------------------|:---------------------------|
| `i16x8.reinterpret/i8x16(a: i8x16) -> i16x8`                  | `-`                        |
| `i16x8.reinterpret/i32x4(a: i32x4) -> i16x8`                  | `-`                        |
| `i16x8.reinterpret/i64x2(a: i64x2) -> i16x8`                  | `-`                        |
| `i16x8.reinterpret/f32x4(a: f32x4) -> i16x8`                  | `-`                        |
| `i16x8.reinterpret/f64x2(a: f64x2) -> i16x8`                  | `-`                        |
| `i16x8.build(x: i16[8]) -> i16x8`                             | `i16x8.build`              |
| `i16x8.splat(x: i16) -> i16x8`                                | `i16x8.splat`              |
| `i16x8.extractLane(a: i16x8, i: LaneIdx8) -> i16`             | `i16x8.extractLane`        |
| `i16x8.replaceLane(a: i16x8, i: LaneIdx8, x: i16) -> i16x8`   | `i16x8.replaceLane`        |
| `i16x8.select(s: b16x8, t: i16x8, f: i16x8) -> i16x8`         | `v16x8.select`             |
| `i16x8.swizzle(a: i16x8, s: LaneIdx8[8]) -> i16x8`            | `v16x8.swizzle`            |
| `i16x8.shuffle(a: i16x8, b: i16x8, s: LaneIdx16[8]) -> i16x8` | `v16x8.shuffle`            |
| `i16x8.add(a: i16x8, b: i16x8) -> i16x8`                      | `i16x8.add`                |
| `i16x8.sub(a: i16x8, b: i16x8) -> i16x8`                      | `i16x8.sub`                |
| `i16x8.mul(a: i16x8, b: i16x8) -> i16x8`                      | `i16x8.mul`                |
| `i16x8.neg(a: i16x8) -> i16x8`                                | `i16x8.neg`                |
| `i16x8.addSaturate_s(a: i16x8, b: i16x8) -> i16x8`            | `s16x8.addSaturate`        |
| `i16x8.addSaturate_u(a: i16x8, b: i16x8) -> i16x8`            | `u16x8.addSaturate`        |
| `i16x8.subSaturate_s(a: i16x8, b: i16x8) -> i16x8`            | `s16x8.subSaturate`        |
| `i16x8.subSaturate_u(a: i16x8, b: i16x8) -> i16x8`            | `u16x8.subSaturate`        |
| `i16x8.shl(a: i16x8, y: i8) -> i16x8`                         | `i16x8.shiftLeftByScalar`  |
| `i16x8.shr_s(a: i16x8, y: i8) -> i16x8`                       | `s16x8.shiftRightByScalar` |
| `i16x8.shr_u(a: i16x8, y: i8) -> i16x8`                       | `u16x8.shiftRightByScalar` |
| `i16x8.and(a: i16x8, b: i16x8) -> i16x8`                      | `v128.and`                 |
| `i16x8.or(a: i16x8, b: i16x8) -> i16x8`                       | `v128.or`                  |
| `i16x8.xor(a: i16x8, b: i16x8) -> i16x8`                      | `v128.xor`                 |
| `i16x8.not(a: i16x8) -> i16x8`                                | `v128.not`                 |
| `i16x8.eq(a: i16x8, b: i16x8) -> b16x8`                       | `i16x8.equal`              |
| `i16x8.ne(a: i16x8, b: i16x8) -> b16x8`                       | `i16x8.notEqual`           |
| `i16x8.lt_s(a: i16x8, b: i16x8) -> b16x8`                     | `s16x8.lessThan`           |
| `i16x8.lt_u(a: i16x8, b: i16x8) -> b16x8`                     | `u16x8.lessThan`           |
| `i16x8.le_s(a: i16x8, b: i16x8) -> b16x8`                     | `s16x8.lessThanOrEqual`    |
| `i16x8.le_u(a: i16x8, b: i16x8) -> b16x8`                     | `u16x8.lessThanOrEqual`    |
| `i16x8.gt_s(a: i16x8, b: i16x8) -> b16x8`                     | `s16x8.greaterThan`        |
| `i16x8.gt_u(a: i16x8, b: i16x8) -> b16x8`                     | `u16x8.greaterThan`        |
| `i16x8.ge_s(a: i16x8, b: i16x8) -> b16x8`                     | `s16x8.greaterThanOrEqual` |
| `i16x8.ge_u(a: i16x8, b: i16x8) -> b16x8`                     | `u16x8.greaterThanOrEqual` |
| `i16x8.load(mem: Buffer, addr: ByteOffset) -> i16x8`          | `v16x8.load`               |
| `i16x8.store(mem: Buffer, addr: ByteOffset, data: i16x8)`     | `v16x8.store`              |

## `i32x4` operations
| WebAssembly                                                  | Portable SIMD              |
|:-------------------------------------------------------------|:---------------------------|
| `i32x4.reinterpret/i8x16(a: i8x16) -> i32x4`                 | `-`                        |
| `i32x4.reinterpret/i16x8(a: i16x8) -> i32x4`                 | `-`                        |
| `i32x4.reinterpret/i64x2(a: i64x2) -> i32x4`                 | `-`                        |
| `i32x4.reinterpret/f32x4(a: f32x4) -> i32x4`                 | `-`                        |
| `i32x4.reinterpret/f64x2(a: f64x2) -> i32x4`                 | `-`                        |
| `i32x4.build(x: i32[4]) -> i32x4`                            | `i32x4.build`              |
| `i32x4.splat(x: i32) -> i32x4`                               | `i32x4.splat`              |
| `i32x4.extractLane(a: i32x4, i: LaneIdx4) -> i32`            | `i32x4.extractLane`        |
| `i32x4.replaceLane(a: i32x4, i: LaneIdx4, x: i32) -> i32x4`  | `i32x4.replaceLane`        |
| `i32x4.select(s: b32x4, t: i32x4, f: i32x4) -> i32x4`        | `v32x4.select`             |
| `i32x4.swizzle(a: i32x4, s: LaneIdx4[4]) -> i32x4`           | `v32x4.swizzle`            |
| `i32x4.shuffle(a: i32x4, b: i32x4, s: LaneIdx8[4]) -> i32x4` | `v32x4.shuffle`            |
| `i32x4.add(a: i32x4, b: i32x4) -> i32x4`                     | `i32x4.add`                |
| `i32x4.sub(a: i32x4, b: i32x4) -> i32x4`                     | `i32x4.sub`                |
| `i32x4.mul(a: i32x4, b: i32x4) -> i32x4`                     | `i32x4.mul`                |
| `i32x4.neg(a: i32x4) -> i32x4`                               | `i32x4.neg`                |
| `i32x4.shl(a: i32x4, y: i8) -> i32x4`                        | `i32x4.shiftLeftByScalar`  |
| `i32x4.shr_s(a: i32x4, y: i8) -> i32x4`                      | `s32x4.shiftRightByScalar` |
| `i32x4.shr_u(a: i32x4, y: i8) -> i32x4`                      | `u32x4.shiftRightByScalar` |
| `i32x4.and(a: i32x4, b: i32x4) -> i32x4`                     | `v128.and`                 |
| `i32x4.or(a: i32x4, b: i32x4) -> i32x4`                      | `v128.or`                  |
| `i32x4.xor(a: i32x4, b: i32x4) -> i32x4`                     | `v128.xor`                 |
| `i32x4.not(a: i32x4) -> i32x4`                               | `v128.not`                 |
| `i32x4.eq(a: i32x4, b: i32x4) -> b32x4`                      | `i32x4.equal`              |
| `i32x4.ne(a: i32x4, b: i32x4) -> b32x4`                      | `i32x4.notEqual`           |
| `i32x4.lt_s(a: i32x4, b: i32x4) -> b32x4`                    | `s32x4.lessThan`           |
| `i32x4.lt_u(a: i32x4, b: i32x4) -> b32x4`                    | `u32x4.lessThan`           |
| `i32x4.le_s(a: i32x4, b: i32x4) -> b32x4`                    | `s32x4.lessThanOrEqual`    |
| `i32x4.le_u(a: i32x4, b: i32x4) -> b32x4`                    | `u32x4.lessThanOrEqual`    |
| `i32x4.gt_s(a: i32x4, b: i32x4) -> b32x4`                    | `s32x4.greaterThan`        |
| `i32x4.gt_u(a: i32x4, b: i32x4) -> b32x4`                    | `u32x4.greaterThan`        |
| `i32x4.ge_s(a: i32x4, b: i32x4) -> b32x4`                    | `s32x4.greaterThanOrEqual` |
| `i32x4.ge_u(a: i32x4, b: i32x4) -> b32x4`                    | `u32x4.greaterThanOrEqual` |
| `i32x4.load(mem: Buffer, addr: ByteOffset) -> i32x4`         | `v32x4.load`               |
| `i32x4.store(mem: Buffer, addr: ByteOffset, data: i32x4)`    | `v32x4.store`              |
| `i32x4.load1(mem: Buffer, addr: ByteOffset) -> i32x4`        | `v32x4.load1`              |
| `i32x4.load2(mem: Buffer, addr: ByteOffset) -> i32x4`        | `v32x4.load2`              |
| `i32x4.load3(mem: Buffer, addr: ByteOffset) -> i32x4`        | `v32x4.load3`              |
| `i32x4.store1(mem: Buffer, addr: ByteOffset, data: i32x4)`   | `v32x4.store1`             |
| `i32x4.store2(mem: Buffer, addr: ByteOffset, data: i32x4)`   | `v32x4.store2`             |
| `i32x4.store3(mem: Buffer, addr: ByteOffset, data: i32x4)`   | `v32x4.store3`             |
| `i32x4.trunc_s(a: f32x4) -> (result: f32x4, fail: boolean)`  | `s32x4.fromFloat`          |
| `i32x4.trunc_u(a: f32x4) -> (result: f32x4, fail: boolean)`  | `u32x4.fromFloat`          |

## `i64x2` operations
| WebAssembly                                                  | Portable SIMD              |
|:-------------------------------------------------------------|:---------------------------|
| `i64x2.reinterpret/i8x16(a: i8x16) -> i64x2`                 | `-`                        |
| `i64x2.reinterpret/i16x8(a: i16x8) -> i64x2`                 | `-`                        |
| `i64x2.reinterpret/i32x4(a: i32x4) -> i64x2`                 | `-`                        |
| `i64x2.reinterpret/f32x4(a: f32x4) -> i64x2`                 | `-`                        |
| `i64x2.reinterpret/f64x2(a: f64x2) -> i64x2`                 | `-`                        |
| `i64x2.build(x: i64[2]) -> i64x2`                            | `i64x2.build`              |
| `i64x2.splat(x: i64) -> i64x2`                               | `i64x2.splat`              |
| `i64x2.extractLane(a: i64x2, i: LaneIdx2) -> i64`            | `i64x2.extractLane`        |
| `i64x2.replaceLane(a: i64x2, i: LaneIdx2, x: i64) -> i64x2`  | `i64x2.replaceLane`        |
| `i64x2.select(s: b64x2, t: i64x2, f: i64x2) -> i64x2`        | `v64x2.select`             |
| `i64x2.swizzle(a: i64x2, s: LaneIdx2[2]) -> i64x2`           | `v64x2.swizzle`            |
| `i64x2.shuffle(a: i64x2, b: i64x2, s: LaneIdx4[2]) -> i64x2` | `v64x2.shuffle`            |
| `i64x2.add(a: i64x2, b: i64x2) -> i64x2`                     | `i64x2.add`                |
| `i64x2.sub(a: i64x2, b: i64x2) -> i64x2`                     | `i64x2.sub`                |
| `i64x2.mul(a: i64x2, b: i64x2) -> i64x2`                     | `i64x2.mul`                |
| `i64x2.neg(a: i64x2) -> i64x2`                               | `i64x2.neg`                |
| `i64x2.shl(a: i64x2, y: i8) -> i64x2`                        | `i64x2.shiftLeftByScalar`  |
| `i64x2.shr_s(a: i64x2, y: i8) -> i64x2`                      | `s64x2.shiftRightByScalar` |
| `i64x2.shr_u(a: i64x2, y: i8) -> i64x2`                      | `u64x2.shiftRightByScalar` |
| `i64x2.and(a: i64x2, b: i64x2) -> i64x2`                     | `v128.and`                 |
| `i64x2.or(a: i64x2, b: i64x2) -> i64x2`                      | `v128.or`                  |
| `i64x2.xor(a: i64x2, b: i64x2) -> i64x2`                     | `v128.xor`                 |
| `i64x2.not(a: i64x2) -> i64x2`                               | `v128.not`                 |
| `i64x2.eq(a: i64x2, b: i64x2) -> b64x2`                      | `i64x2.equal`              |
| `i64x2.ne(a: i64x2, b: i64x2) -> b64x2`                      | `i64x2.notEqual`           |
| `i64x2.lt_s(a: i64x2, b: i64x2) -> b64x2`                    | `s64x2.lessThan`           |
| `i64x2.lt_u(a: i64x2, b: i64x2) -> b64x2`                    | `u64x2.lessThan`           |
| `i64x2.le_s(a: i64x2, b: i64x2) -> b64x2`                    | `s64x2.lessThanOrEqual`    |
| `i64x2.le_u(a: i64x2, b: i64x2) -> b64x2`                    | `u64x2.lessThanOrEqual`    |
| `i64x2.gt_s(a: i64x2, b: i64x2) -> b64x2`                    | `s64x2.greaterThan`        |
| `i64x2.gt_u(a: i64x2, b: i64x2) -> b64x2`                    | `u64x2.greaterThan`        |
| `i64x2.ge_s(a: i64x2, b: i64x2) -> b64x2`                    | `s64x2.greaterThanOrEqual` |
| `i64x2.ge_u(a: i64x2, b: i64x2) -> b64x2`                    | `u64x2.greaterThanOrEqual` |
| `i64x2.load(mem: Buffer, addr: ByteOffset) -> i64x2`         | `v64x2.load`               |
| `i64x2.store(mem: Buffer, addr: ByteOffset, data: i64x2)`    | `v64x2.store`              |
| `i64x2.trunc_s(a: f64x2) -> (result: f64x2, fail: boolean)`  | `s64x2.fromFloat`          |
| `i64x2.trunc_u(a: f64x2) -> (result: f64x2, fail: boolean)`  | `u64x2.fromFloat`          |

## `f32x4` operations
| WebAssembly                                                   | Portable SIMD                       |
|:--------------------------------------------------------------|:------------------------------------|
| `f32x4.reinterpret/i8x16(a: i8x16) -> f32x4`                  | `-`                                 |
| `f32x4.reinterpret/i16x8(a: i16x8) -> f32x4`                  | `-`                                 |
| `f32x4.reinterpret/i32x4(a: i32x4) -> f32x4`                  | `-`                                 |
| `f32x4.reinterpret/i64x2(a: i64x2) -> f32x4`                  | `-`                                 |
| `f32x4.reinterpret/f64x2(a: f64x2) -> f32x4`                  | `-`                                 |
| `f32x4.build(x: f32[4]) -> f32x4`                             | `f32x4.build`                       |
| `f32x4.splat(x: f32) -> f32x4`                                | `f32x4.splat`                       |
| `f32x4.extractLane(a: f32x4, i: LaneIdx4) -> f32`             | `f32x4.extractLane`                 |
| `f32x4.replaceLane(a: f32x4, i: LaneIdx4, x: f32) -> f32x4`   | `f32x4.replaceLane`                 |
| `f32x4.select(s: b32x4, t: f32x4, f: f32x4) -> f32x4`         | `v32x4.select`                      |
| `f32x4.swizzle(a: f32x4, s: LaneIdx4[4]) -> f32x4`            | `v32x4.swizzle`                     |
| `f32x4.shuffle(a: f32x4, b: f32x4, s: LaneIdx8[4]) -> f32x4`  | `v32x4.shuffle`                     |
| `f32x4.add(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | `f32x4.add`                         |
| `f32x4.sub(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | `f32x4.sub`                         |
| `f32x4.mul(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | `f32x4.mul`                         |
| `f32x4.neg(a: f32x4) -> f32x4`                                | `f32x4.neg`                         |
| `f32x4.and(a: f32x4, b: f32x4) -> f32x4`                      | `v128.and`                          |
| `f32x4.or(a: f32x4, b: f32x4) -> f32x4`                       | `v128.or`                           |
| `f32x4.xor(a: f32x4, b: f32x4) -> f32x4`                      | `v128.xor`                          |
| `f32x4.not(a: f32x4) -> f32x4`                                | `v128.not`                          |
| `f32x4.eq(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.equal`                       |
| `f32x4.ne(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.notEqual`                    |
| `f32x4.lt(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.lessThan`                    |
| `f32x4.le(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.lessThanOrEqual`             |
| `f32x4.gt(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.greaterThan`                 |
| `f32x4.ge(a: f32x4, b: f32x4) -> b32x4`                       | `f32x4.greaterThanOrEqual`          |
| `f32x4.load(mem: Buffer, addr: ByteOffset) -> f32x4`          | `v32x4.load`                        |
| `f32x4.store(mem: Buffer, addr: ByteOffset, data: f32x4)`     | `v32x4.store`                       |
| `f32x4.load1(mem: Buffer, addr: ByteOffset) -> f32x4`         | `v32x4.load1`                       |
| `f32x4.load2(mem: Buffer, addr: ByteOffset) -> f32x4`         | `v32x4.load2`                       |
| `f32x4.load3(mem: Buffer, addr: ByteOffset) -> f32x4`         | `v32x4.load3`                       |
| `f32x4.store1(mem: Buffer, addr: ByteOffset, data: f32x4)`    | `v32x4.store1`                      |
| `f32x4.store2(mem: Buffer, addr: ByteOffset, data: f32x4)`    | `v32x4.store2`                      |
| `f32x4.store3(mem: Buffer, addr: ByteOffset, data: f32x4)`    | `v32x4.store3`                      |
| `f32x4.abs(a: f32x4) -> f32x4`                                | `f32x4.abs`                         |
| `f32x4.min(a: f32x4, b: f32x4) -> f32x4`                      | `f32x4.min`                         |
| `f32x4.max(a: f32x4, b: f32x4) -> f32x4`                      | `f32x4.max`                         |
| `f32x4.minNum(a: f32x4, b: f32x4) -> f32x4`                   | `f32x4.minNum`                      |
| `f32x4.maxNum(a: f32x4, b: f32x4) -> f32x4`                   | `f32x4.maxNum`                      |
| `f32x4.div(a: f32x4, b: f32x4, rmode: RoundingMode) -> f32x4` | `f32x4.div`                         |
| `f32x4.sqrt(a: f32x4, rmode: RoundingMode) -> f32x4`          | `f32x4.sqrt`                        |
| `f32x4.reciprocalApproximation(a: f32x4) -> f32x4`            | `f32x4.reciprocalApproximation`     |
| `f32x4.reciprocalSqrtApproximation(a: f32x4) -> f32x4`        | `f32x4.reciprocalSqrtApproximation` |
| `f32x4.convert_s(a: i32x4, rmode: RoundingMode) -> f32x4`     | `f32x4.fromSignedInt`               |
| `f32x4.convert_u(a: i32x4, rmode: RoundingMode) -> f32x4`     | `f32x4.fromUnsignedInt`             |

## `f64x2` operations
| WebAssembly                                                   | Portable SIMD                       |
|:--------------------------------------------------------------|:------------------------------------|
| `f64x2.reinterpret/i8x16(a: i8x16) -> f64x2`                  | `-`                                 |
| `f64x2.reinterpret/i16x8(a: i16x8) -> f64x2`                  | `-`                                 |
| `f64x2.reinterpret/i32x4(a: i32x4) -> f64x2`                  | `-`                                 |
| `f64x2.reinterpret/i64x2(a: i64x2) -> f64x2`                  | `-`                                 |
| `f64x2.reinterpret/f32x4(a: f32x4) -> f64x2`                  | `-`                                 |
| `f64x2.build(x: f64[2]) -> f64x2`                             | `f64x2.build`                       |
| `f64x2.splat(x: f64) -> f64x2`                                | `f64x2.splat`                       |
| `f64x2.extractLane(a: f64x2, i: LaneIdx2) -> f64`             | `f64x2.extractLane`                 |
| `f64x2.replaceLane(a: f64x2, i: LaneIdx2, x: f64) -> f64x2`   | `f64x2.replaceLane`                 |
| `f64x2.select(s: b64x2, t: f64x2, f: f64x2) -> f64x2`         | `v64x2.select`                      |
| `f64x2.swizzle(a: f64x2, s: LaneIdx2[2]) -> f64x2`            | `v64x2.swizzle`                     |
| `f64x2.shuffle(a: f64x2, b: f64x2, s: LaneIdx4[2]) -> f64x2`  | `v64x2.shuffle`                     |
| `f64x2.add(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | `f64x2.add`                         |
| `f64x2.sub(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | `f64x2.sub`                         |
| `f64x2.mul(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | `f64x2.mul`                         |
| `f64x2.neg(a: f64x2) -> f64x2`                                | `f64x2.neg`                         |
| `f64x2.and(a: f64x2, b: f64x2) -> f64x2`                      | `v128.and`                          |
| `f64x2.or(a: f64x2, b: f64x2) -> f64x2`                       | `v128.or`                           |
| `f64x2.xor(a: f64x2, b: f64x2) -> f64x2`                      | `v128.xor`                          |
| `f64x2.not(a: f64x2) -> f64x2`                                | `v128.not`                          |
| `f64x2.eq(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.equal`                       |
| `f64x2.ne(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.notEqual`                    |
| `f64x2.lt(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.lessThan`                    |
| `f64x2.le(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.lessThanOrEqual`             |
| `f64x2.gt(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.greaterThan`                 |
| `f64x2.ge(a: f64x2, b: f64x2) -> b64x2`                       | `f64x2.greaterThanOrEqual`          |
| `f64x2.load(mem: Buffer, addr: ByteOffset) -> f64x2`          | `v64x2.load`                        |
| `f64x2.store(mem: Buffer, addr: ByteOffset, data: f64x2)`     | `v64x2.store`                       |
| `f64x2.abs(a: f64x2) -> f64x2`                                | `f64x2.abs`                         |
| `f64x2.min(a: f64x2, b: f64x2) -> f64x2`                      | `f64x2.min`                         |
| `f64x2.max(a: f64x2, b: f64x2) -> f64x2`                      | `f64x2.max`                         |
| `f64x2.minNum(a: f64x2, b: f64x2) -> f64x2`                   | `f64x2.minNum`                      |
| `f64x2.maxNum(a: f64x2, b: f64x2) -> f64x2`                   | `f64x2.maxNum`                      |
| `f64x2.div(a: f64x2, b: f64x2, rmode: RoundingMode) -> f64x2` | `f64x2.div`                         |
| `f64x2.sqrt(a: f64x2, rmode: RoundingMode) -> f64x2`          | `f64x2.sqrt`                        |
| `f64x2.reciprocalApproximation(a: f64x2) -> f64x2`            | `f64x2.reciprocalApproximation`     |
| `f64x2.reciprocalSqrtApproximation(a: f64x2) -> f64x2`        | `f64x2.reciprocalSqrtApproximation` |
| `f64x2.convert_s(a: i64x2, rmode: RoundingMode) -> f64x2`     | `f64x2.fromSignedInt`               |
| `f64x2.convert_u(a: i64x2, rmode: RoundingMode) -> f64x2`     | `f64x2.fromUnsignedInt`             |
