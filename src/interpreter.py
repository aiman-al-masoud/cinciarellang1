from compiler.char_stream import CharStream
from compiler.token_stream import TokenStream
from compiler.parser import Parser
from runtime.runtime import Runtime
from runtime.enviro import Enviro

class Interpreter:

    def __init__(self):
        self.rt = Runtime()
        self.rt.env.set("eval", Eval(self.rt.eval, self.eval))
        self.rt.env.set("import", Import(self.rt.eval, self.eval))


    def eval(self, string:str):

        o = None
        for stm in Parser(TokenStream(CharStream(string+";"))).parse():
            o = self.rt.eval(stm)

        return o


class Eval:

    def __init__(self, eval_ast, eval_source):
        self.eval_ast = eval_ast
        self.eval_source = eval_source

    def run(self, args, env:Enviro):
        source = self.eval_ast(args[0])
        return self.eval_source(source)


class Import:

    def __init__(self, eval_ast, eval_source):
        self.eval_ast = eval_ast
        self.eval_source = eval_source

    def run(self, args, env:Enviro):
        path = self.eval_ast(args[0])
        print("path", path)
        exit()
        with open(path) as f:
            source = f.read()
        self.eval_source(source)