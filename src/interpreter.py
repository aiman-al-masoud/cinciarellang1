from compiler.char_stream import CharStream
from compiler.token_stream import TokenStream
from compiler.parser import Parser
from runtime.runtime import Runtime

class Interpreter:

    def __init__(self):
        self.rt = Runtime()

    def eval(self, string:str):

        o = None
        for stm in Parser(TokenStream(CharStream(string+";"))).parse():
            o = self.rt.eval(stm)

        return o