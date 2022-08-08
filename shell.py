from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser
from interpreter import Interpreter

# REPL
while True:

    s = "true || false;"
    p = Parser(TokenStream(CharStream(s)))
    prg = p.parse()


    i = Interpreter()
    r = i.eval(prg[0])

    print(r)

