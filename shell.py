from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser
from interpreter import Interpreter

i = Interpreter()

# REPL
while True:

    s = input()
    p = Parser(TokenStream(CharStream(s)))

    r = None
    for stm in p.parse():
        r = i.eval(stm)

    print(r)
