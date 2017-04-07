#
# Represent portable SIMD spec objects
#
import re
from typing import List, Tuple, Dict  # noqa


class Interpretation(object):
    '''One of the SIMD types or interpretations'''

    def __init__(self, name: str) -> None:
        self.name = name
        self.parent = None  # type: Interpretation
        self.children = list()  # type: List[Interpretation]
        # Operations defined directly on this interpretation.
        self.operations = list()  # type: List[Operation]

    def __repr__(self) -> str:
        return 'Interpretation({})'.format(self.name)

    def __str__(self) -> str:
        return self.name

    def pre(self) -> Tuple['Interpretation', ...]:
        '''
        Get a tuple containing a pre-order of all the children, starting with
        self.
        '''
        return sum([c.pre() for c in self.children], (self,))


class Operation(object):
    '''
    A SIMD operation as identified by name only.

    The 'add' operation is represented by one `Operation` object covering
    `i32x4.add`, `i8x16.add`, ...
    '''

    def __init__(self, name: str) -> None:
        self.name = name
        self.signatures = dict()  # type: Dict[Interpretation, Signature]

    def __str__(self) -> str:
        return self.name

    def add_signature(self, interp: Interpretation, sig: 'Signature') -> None:
        assert interp not in self.signatures, "Duplicate signature"
        self.signatures[interp] = sig

    def get_definition(self, interp: Interpretation) -> Interpretation:
        '''
        Get the Interpretation where this operation is defined for
        `interp`.

        This can be either `interp` itself or one of its parents.
        '''
        while interp:
            if interp in self.signatures:
                return interp
            interp = interp.parent
        return None


class Signature(object):
    '''
    A specific SIMD operation signature.

    For the 'add'` operation, there are signatures for `i32x4.add`,
    `i8x16.add`, etc. The signature ties operations and interpretations
    together and stores the arguments and results too.

    The `anchor` argument refers to the section of the spec where the Signature
    is defined.
    '''

    def __init__(
            self,
            interpretation: Interpretation,
            operation: Operation,
            args: str,
            result: str,
            anchor: str
            ) -> None:
        self.interpretation = interpretation
        self.operation = operation
        self.args = args
        self.result = result
        self.anchor = anchor

    def with_result(self, new_result: str) -> 'Signature':
        '''Return a new signature with a new result type'''
        return Signature(
                self.interpretation, self.operation, self.args, new_result,
                self.anchor)

    def mdlink(self, ext: str = 'md') -> str:
        '''Get a Markdown link to this specification.'''
        return '[{}.{}](portable-simd.{}{})'.format(
                self.interpretation, self.operation, ext, self.anchor)


class Specification(object):
    '''Collection of SIMD specification objects'''

    def __init__(self) -> None:
        # List of types/interpretations in order of appearance.
        self.interpretations = list()  # type: List[Interpretation]
        self.interpretations_byname = dict()  # type: Dict[str, Interpretation]
        self.operations = list()  # type: List[Operation]
        self.operations_byname = dict()  # type: Dict[str, Operation]

    def interpretations_pre(self) -> Tuple[Interpretation, ...]:
        '''
        Get a tuple containing a pre-order of all the interpretations.
        '''
        return sum(
                [it.pre() for it in self.interpretations
                    if it.parent is None], ())

    def add_interpretation(self, interp: Interpretation) -> None:
        '''Register a new Interpretation object'''
        assert interp.name not in self.interpretations_byname, "Duplicate"
        self.interpretations.append(interp)
        self.interpretations_byname[interp.name] = interp

    def get_operation(self, name: str) -> Operation:
        '''
        Get an `Operation` object with the requested name.

        Create a new object if thisis the first time `name` is seen
        '''
        if name in self.operations_byname:
            return self.operations_byname[name]
        op = Operation(name)
        self.operations.append(op)
        self.operations_byname[name] = op
        return op

    def extract_interpretations(self, text: str) -> None:
        '''
        Find new `Interpretation` declarations in the text, add them to spec.
        '''
        # Definitions look like:
        #
        # * `i32x4 : v32x4`: ...
        #
        for m in re.finditer(
                r'^\* `([visufb][0-9x]+)( : ([visufb][0-9x]+))?`', text,
                re.MULTILINE):
            interp = Interpretation(m.group(1))
            pname = m.group(3)
            if pname:
                interp.parent = self.interpretations_byname[pname]
                interp.parent.children.append(interp)
            self.add_interpretation(interp)

    def extract_operations(
            self, text: str
            ) -> List[Tuple[Interpretation, Operation]]:
        '''Find new `Operation` declarations in the text.'''
        # Operations look like:
        #
        # * `i32x4.add(a : v128, b : v128) -> v128`
        #
        found = list()  # type: List[Tuple[Interpretation, Operation]]
        anchor = None
        for m in re.finditer(
                r'^#+\s*(.*)|' +
                r'^\* `(?P<it>[visufb][0-9x]+)\.' +
                r'(?P<op>\w+)\((?P<args>[^)]*)\)\s*(->\s*(?P<res>.*))?`', text,
                re.MULTILINE):
            if m.group(0).startswith('#'):
                # This is a section header.
                anchor = '#' + '-'.join(m.group(1).lower().split())
                continue

            interp = self.interpretations_byname[m.group('it')]
            op = self.get_operation(m.group('op'))
            args = m.group('args')
            result = m.group('res')
            op.add_signature(
                    interp, Signature(interp, op, args, result, anchor))
            interp.operations.append(op)
            found.append((interp, op))
        return found

    def parse(self, text: str) -> None:
        '''Parse the spec text and add all definitions to self'''
        self.extract_interpretations(text)
        self.extract_operations(text)
