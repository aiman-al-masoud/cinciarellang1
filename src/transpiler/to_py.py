class ToPy:

    """
    Converts the AST into readable Python 3 code.
    TODO: deal with get, set, obj, eval, chirp and import Cinciarellang funcs.
    """

    def eval(self, ast):

        if ast is None:
            return 
    
        if ast['type'] in ['num', 'id']:
            return str(ast['val'])

        if ast['type'] == 'str':
            return f"\"{ast['val']}\""


        if ast['type'] == 'bool':
            return str(ast['val']).capitalize()

        if ast['type'] == '=':
            lv = self.eval(ast['left'])
            rv = ast['right']

            if rv['type'] == 'fun':
                return self.make_fun(lv, rv['params'], rv['body'])
            else:
                return f"{lv} = {self.eval(rv)}"

        if ast['type'] in ['add', 'sub', 'mul', 'div', 'or', 'and', '==', '!=', '>', '<', '>=', '<=']:
            return self.bin_op(ast['type'], self.eval(ast['left']), self.eval(ast['right']))

        if ast['type'] in ['-', '!']:
            return self.un_op(ast['type'], self.eval(ast['arg']))

        if ast['type'] == 'block':
            blk = ""
            for stm in ast['val']:
                blk+=self.eval(stm)+"\n"
            return blk

        if ast['type'] == 'if':
            cond = self.eval(ast['cond'])
            then =  self.eval(ast['then']) 
            _else =  self.eval(ast['else'])
            return f"if {cond}:\n    {then}\nelse:\n    {_else}"

        if ast['type'] == 'fun':
            return "" # see assignment (above)

        if ast['type'] == 'call':
            name = ast['name']['val']
            args = ", ".join( str(self.eval(a)) for a in ast['args'])
            return f"{name}({args})"
            

    def bin_op(self, op:str, left, right):
        
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

    def un_op(self, op:str, arg):

        if op == '-':
            return f"-{arg}"
        if op == '!':
            return f"not {arg}"

    def make_fun(self, name, params, body):

        body = [l for l in self.eval(body).split("\n") if l.strip() != ""]
        ret = "return "+body.pop()
        body.append(ret)
        body = "\n    " + "\n    ".join(body)
        params = ", ".join([p['val'] for p in params])
        return f"def {name}({params}):{body}"



# def main():

#     s = """
#     x = (1 > 1) || !true;
#     y = 1+1;
#     if true{
#         x = 1;
#     };    
#     """

#     s = """
#     f = fun(x, y){
#         x + y;
#         x = 1;
#         x;
#     };

#     f(1, 2);
#     g = f;
#     """ 

#     # s = "f(1,2,a);"

#     astls = Parser(TokenStream(CharStream(s))).parse()

#     for ast in astls:

#         ps = ToPy().eval(ast)
#         print(ps)



# def main2():

#     import sys
#     with open(sys.argv[1]) as f:
#         s = f.read()

#     astls = Parser(TokenStream(CharStream(s))).parse()
#     for ast in astls:
#         print(ToPy().eval(ast))

    

    
# if __name__ == '__main__':
#     main2()