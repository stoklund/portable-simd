#!/usr/bin/env python
#
# Generate webassembly-opcodes.md containing all the WebAssembly SIMD opcodes.
#
import re
import simdspec

spec = simdspec.Specification()
with open('portable-simd.md') as f:
    spec.parse(f.read())

print('''
# WebAssembly SIMD operations

This table is generated automatically from [the
specification](portable-simd.md) using [the WebAssembly
mapping](webassembly-mapping.md).
''')

# Get the interpretations that correspond to Wasm types.
wasm = [it for it in spec.interpretations if len(it.operations) > 0 and
        it.name[0] in 'ifb']

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
# sig: (args, result) tuple from Operation.
# res_type: String with the name of the result SIMD type.
# arg_type: None, or name of argument SIMD type. Defaults to res_type.
def format_sig(name, sig, res_type, arg_type=None):
    if arg_type is None:
        arg_type = res_type
    args, result = sig
    args = re.sub(r'\b(i8|i16|boolean)\b', 'i32', args)
    args = args.replace('v128', arg_type)
    if result is None:
        return '{}({})'.format(name, args)
    else:
        result = result.replace('v128', res_type).replace('boolean', 'i32')
        return '{}({}) {}'.format(name, args, result)


# Yield tuples (wsig, psig) for each wasm operation on interpretation `it`.
def wasm_sigs(it):
    # Pre-order of children, self removed.
    children = it.pre()[1:]

    # Generate bit cast operations.
    if it.name[0] != 'b':
        for from_it in (i.name for i in wasm if i != it and i.name[0] != 'b'):
            wsig = '{}.reinterpret/{}(a: {}) -> {}'.format(
                    it.name, from_it, from_it, it.name)
            yield (wsig, '')

    # Generate real operations.
    for op in spec.operations:
        op_name = '{}.{}'.format(it.name, name_map.get(op.name, op.name))
        op_it = op.get_definition(it)
        if op_it:
            # This operation has a definition for `it` or one of its parents.
            psig = '{}.{}'.format(op_it.name, op.name)
            sig = op.signatures[op_it]
            arg_type = it.name
            # Special cases where arg_type != res_type.
            if op.name in ('fromSignedInt', 'fromUnsignedInt'):
                arg_type = 'i' + it.name[1:]
            # Create s/u variants for functions that have i8/i16 results.
            if sig[1] in ('-> i8', '-> i16'):
                sig = (sig[0], '-> i32')
                yield (format_sig(op_name+'_s', sig, it.name, arg_type), psig)
                yield (format_sig(op_name+'_u', sig, it.name, arg_type), psig)
            else:
                wsig = format_sig(op_name, sig, it.name, arg_type)
                yield (wsig, psig)
        else:
            # Check for child interpretation definitions.
            for ch_it in children:
                if op.get_definition(ch_it) == ch_it:
                    sig = op.signatures[ch_it]
                    arg_type = it.name
                    # Special cases where arg_type != res_type.
                    if op.name in ('fromFloat'):
                        arg_type = 'f' + it.name[1:]
                    # Create a '_s' or _u suffixed opcode.
                    suffixed = '{}_{}'.format(op_name, ch_it.name[0])
                    wsig = format_sig(suffixed, sig, it.name, arg_type)
                    psig = '{}.{}'.format(ch_it.name, op.name)
                    yield (wsig, psig)

for it in wasm:
    print('')
    print('## `{}` operations'.format(it.name))
    sigs = list(wasm_sigs(it))
    maxw = 2 + max(len(w) for w, p in sigs)
    maxp = 2 + max(len(p) for w, p in sigs)

    print('| {} | {} |'.format('WebAssembly'.ljust(maxw),
                'Portable SIMD'.ljust(maxp)))
    print('|:{}-|:{}-|'.format('-' * maxw, '-' * maxp))
    for wsig, psig in sigs:
        wsig = '`{}`'.format(wsig)
        if psig == '':
            psig = '-'
        else:
            psig = '`{}`'.format(psig)
        print('| {} | {} |'.format(wsig.ljust(maxw), psig.ljust(maxp)))
