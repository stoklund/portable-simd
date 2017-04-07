#!/usr/bin/env python
#
# Generate webassembly-opcodes.md containing all the WebAssembly SIMD opcodes.
#
import re
import simdspec
from typing import Tuple, Iterable

spec = simdspec.Specification()
with open('portable-simd.md') as f:
    spec.parse(f.read())

print('''
# WebAssembly SIMD operations

This table is generated automatically from [the
specification](portable-simd.md) using [the WebAssembly
mapping](webassembly-mapping.md).
''')

# Get the interpretations that correspond to the WebAssembly opcode naming
# scheme: vxxx, ints, floats, and bools. Unsigned/signed are represented as
# `_u` and `_s` suffixes instead.
wasm = [it for it in spec.interpretations_pre()
        if len(it.operations) > 0 and it.name[0] in 'vifb']


# Begin with a table of links to the interpretations, except for `v128`.
def print_toc() -> None:
    print('''
The SIMD operations are grouped according to the interpretation of the input
and output vectors.

| Shape | Int | Float | Bool |
|:-----:|:---:|:-----:|:----:|''')

    for shape in ('8x16', '16x8', '32x4', '64x2'):
        for prefix in 'vifb':
            it = prefix + shape
            if it in spec.interpretations_byname:
                print('| [{it}](#{it}-operations) '.format(it=it), end='')
            else:
                print('| - ', end='')
        print('|')


# Mapping table for operation name stems. The `type.` prefix and any `_u` or
# `_s` suffixes are added automatically.
name_map = {
        'shiftLeftByScalar': 'shl',
        'shiftRightByScalar': 'shr',
        'equal': 'eq',
        'notEqual': 'ne',
        'lessThan': 'lt',
        'lessThanOrEqual': 'le',
        'greaterThan': 'gt',
        'greaterThanOrEqual': 'ge',
        'fromFloat': 'trunc',
        'fromSignedInt': 'convert_s',
        'fromUnsignedInt': 'convert_u'
        }


# Format a signature for wasm.
#
# name: Name of the wasm opcode.
# sig: Signature from Operation.
def format_sig(
        name: str,
        sig: simdspec.Signature,
        ) -> str:
    args = re.sub(r'\b(i8|i16|boolean)\b', 'i32', sig.args)
    if sig.result is None:
        return '{}({})'.format(name, args)
    else:
        result = sig.result.replace('boolean', 'i32')
        return '{}({}) -> {}'.format(name, args, result)


# Yield tuples (wsig, psig) for each wasm operation on interpretation
# `it`.
def wasm_sigs(
        it: simdspec.Interpretation
        ) -> Iterable[Tuple[str, simdspec.Signature]]:
    # Pre-order of children, self removed.
    children = it.pre()[1:]

    for op in spec.operations:
        # These operations are not mapped to WebAssembly.
        if op.name in ('minNum', 'maxNum'):
            continue
        op_name = '{}.{}'.format(it.name, name_map.get(op.name, op.name))
        op_it = op.get_definition(it)
        if op_it == it:
            # This operation has a definition for `it`.
            sig = op.signatures[op_it]
            # Append input argument types: `convert_s/i32x4`
            if op.name in ('fromSignedInt', 'fromUnsignedInt'):
                op_name += '/i' + it.name[1:]
            # Create s/u variants for functions that have i8/i16 results.
            if sig.result in ('i8', 'i16'):
                sig = sig.with_result('i32')
                yield (format_sig(op_name+'_s', sig), sig)
                yield (format_sig(op_name+'_u', sig), sig)
            else:
                yield (format_sig(op_name, sig), sig)
        elif op_it is None and it.name[0] == 'i':
            # Check for child interpretation definitions for integer
            # interpretations.
            for ch_it in children:
                if op.get_definition(ch_it) == ch_it:
                    sig = op.signatures[ch_it]
                    if op.name in ('fromFloat',):
                        # Replace the (result, fail) result tuple.
                        # This operation traps in wasm.
                        sig = sig.with_result('v128')
                        suffixed = '{}_{}/f{}'.format(
                                op_name, ch_it.name[0], it.name[1:])
                    else:
                        # Create a '_s' or _u suffixed opcode.
                        suffixed = '{}_{}'.format(op_name, ch_it.name[0])
                    wsig = format_sig(suffixed, sig)
                    yield (wsig, sig)


print_toc()
for it in wasm:
    print('')
    print('## `{}` operations'.format(it.name))
    sigs = list(wasm_sigs(it))
    maxw = 2 + max(len(w) for w, p in sigs)

    print('| {} | {} |'.format('WebAssembly'.ljust(maxw), 'Portable SIMD'))
    print('|:{}-|:--------------|'.format('-' * maxw))
    for wsig, psig in sigs:
        wsig = '`{}`'.format(wsig)
        if psig:
            str_psig = psig.mdlink()
        else:
            str_psig = '-'
        print('| {} | {} |'.format(wsig.ljust(maxw), str_psig))
