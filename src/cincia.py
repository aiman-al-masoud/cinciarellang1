#!/bin/python3
import sys, readline # shell history
from interpreter import Interpreter
from transpiler.to_py import ToPy
from compiler.char_stream import CharStream
from compiler.token_stream import TokenStream
from compiler.parser import Parser

inter = Interpreter()


# transpile to python mode
if len(sys.argv) == 3:
    opt = sys.argv[1] # -c --compile

    if opt not in ["-c", "--compile"]:
        print("Invalid option! Use -c or --compile")
        exit(0)

    path = sys.argv[2]

    with open(path) as f:
       s = f.read()

    for ast in Parser(TokenStream(CharStream(s))).parse():
        print(ToPy().eval(ast))

    exit(0)


# batch mode
if len(sys.argv) == 2:
    path = sys.argv[1]
    with open(path) as f:
        inter.eval(f.read())
    exit(0)

# REPL mode
while True:
    i = input("> ")
    o = inter.eval(i)
    if o is not None: print( str(o).lower() if o in [True , False] else o )
