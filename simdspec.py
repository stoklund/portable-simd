#
# Represent portable SIMD spec objects
#
import re


class Interpretation(object):
    '''One of the SIMD types or interpretations'''

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = list()
        # Operations defined directly on this interpretation.
        self.operations = list()

    def __repr__(self):
        return 'Interpretation({})'.format(self.name)

    def __str__(self):
        return self.name

    def pre(self):
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

    def __init__(self, name):
        self.name = name
        # Map Interpretation -> signature.
        self.signatures = dict()

    def __str__(self):
        return self.name

    def add_signature(self, interp, sig):
        assert interp not in self.signatures, "Duplicate signature"
        self.signatures[interp] = sig

    def get_definition(self, interp):
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

    def __init__(self, interpretation, operation, args, result, anchor):
        self.interpretation = interpretation
        self.operation = operation
        self.args = args
        self.result = result
        self.anchor = anchor

    def with_result(self, new_result):
        '''Return a new signature with a new result type'''
        return Signature(
                self.interpretation, self.operation, self.args, new_result,
                self.anchor)

    def mdlink(self, ext='md'):
        '''Get a Markdown link to this specification.'''
        return '[{}.{}](portable-simd.{}{})'.format(
                self.interpretation, self.operation, ext, self.anchor)


class Specification(object):
    '''Collection of SIMD specification objects'''

    def __init__(self):
        # List of types/interpretations in order of appearence.
        self.interpretations = list()
        self.interpretations_byname = dict()
        self.operations = list()
        self.operations_byname = dict()

    def add_interpretation(self, interp):
        '''Register a new Interpretation object'''
        assert interp.name not in self.interpretations_byname, "Duplicate"
        self.interpretations.append(interp)
        self.interpretations_byname[interp.name] = interp

    def get_operation(self, name):
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

    def extract_interpretations(self, text):
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

    def extract_operations(self, text):
        '''Find new `Operation` declarations in the text.'''
        # Operations look like:
        #
        # * `i32x4.add(a : v128, b : v128) -> v128`
        #
        found = list()
        anchor = None
        for m in re.finditer(
                r'^#+\s*(.*)|' +
                r'^\* `(?P<it>[visufb][0-9x]+)\.' +
                r'(?P<op>\w+)\((?P<args>.*)\)\s*(->\s*(?P<res>.*))?`', text,
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

    def parse(self, text):
        '''Parse the spec text and add all definitions to self'''
        self.extract_interpretations(text)
        self.extract_operations(text)
