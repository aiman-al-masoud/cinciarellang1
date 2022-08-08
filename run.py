#!/bin/python3

from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser
from interpreter import Interpreter
import sys

path = sys.argv[1]

with open(path) as f:
    s = f.read()


i = Interpreter()
statements = Parser(TokenStream(CharStream(s))).parse()

r = None 
for stm in statements:
    r = i.eval(stm)

if r:
    print(r)
