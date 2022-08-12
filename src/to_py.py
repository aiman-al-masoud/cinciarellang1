from compiler.char_stream import CharStream
from compiler.token_stream import TokenStream
from compiler.parser import Parser

# transpiler

class ToPy:

    def eval(self, ast):
    
        if ast['type'] in ['num', 'str', 'id']:
            return str(ast['val'])

        if ast['type'] == 'bool':
            return str(ast['val']).capitalize()

        if ast['type'] == '=':
            lv = self.eval(ast['left'])
            rv = self.eval(ast['right'])
            return f"{lv} = {rv}"

        if ast['type'] in ['add', 'sub', 'mul', 'div', 'or', 'and', '==', '!=', '>', '<', '>=', '<=']:
            return self.apply_op(ast['type'], self.eval(ast['left']), self.eval(ast['right']))

    def apply_op(self, op:str, left, right):
        
        if op == 'add':
            return f"{left} + {right}"
        if op == 'sub':
            return f"{left} - {right}"
        if op == 'mul':
            return f"{left} * {right}"
        if op == 'div':
            return f"{left} / {right}"
        if op == 'or':
            return f"{left} or {right}"
        if op == 'and':
            return f"{left} and {right}"
        if op == '==':
            return f"{left} == {right}"
        if op == '!=':
            return f"{left} != {right}"
        if op == '>':
            return f"{left} > {right}"
        if op == '<':
            return f"{left} < {right}"
        if op == '>=':
            return f"{left} >= {right}"
        if op == '<=':
            return f"{left} <= {right}"



def main():
    s = "x = (1 > 1) || true;"
    ast = Parser(TokenStream(CharStream(s))).parse()[0]
    ps = ToPy().eval(ast)
    print(ps)


if __name__ == '__main__':
    main()