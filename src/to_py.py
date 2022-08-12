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



def main():
    s = "x = true;"
    ast = Parser(TokenStream(CharStream(s))).parse()[0]
    ps = ToPy().eval(ast)
    print(ps)


if __name__ == '__main__':
    main()