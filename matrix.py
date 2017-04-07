#!/usr/bin/env python
#
# Generate matrix.md containing a matrix of SIMD types and methods.
#
import simdspec

spec = simdspec.Specification()
with open('portable-simd.md') as f:
    spec.parse(f.read())

print('''
# SIMD operations

This table is generated automatically from [the
specification](portable-simd.md). For each SIMD type or interpretation, the
table indicates a **Y** when the operation has a definition specialized to this
interpretation.

When an operation is inherited from a less specific interpretation, that
interpretation is listed.

''')

simd = [it for it in spec.interpretations if len(it.operations) > 0 and
        len(it.children) == 0]
maxoname = max(len(op.name) for op in spec.operations)
maxiname = max(len(it.name) for it in simd)

print('| {} | {} |'.format(
    'Operation'.ljust(maxoname),
    ' | '.join(it.name.center(maxiname) for it in simd)))
print('|-{}-|:{}:|'.format(
    '-'*maxoname, ':|:'.join('-'*maxiname for it in simd)))

for op in spec.operations:
    line = list()
    for interp in simd:
        d = op.get_definition(interp)
        if d is interp:
            line.append('Y')
        else:
            line.append(d.name if d else '')
    print('| {} | {} |'.format(
        op.name.ljust(maxoname),
        ' | '.join(s.center(maxiname) for s in line)))
