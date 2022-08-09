#!/bin/python3
import sys, readline # shell history
from interpreter import Interpreter

inter = Interpreter()

# batch mode
if len(sys.argv) > 1:
    path = sys.argv[1]
    with open(path) as f:
        inter.eval(f.read())
    exit(0)

# REPL mode
while True:
    i = input("> ")
    o = inter.eval(i)
    if o is not None: print( str(o).lower() if o in [True , False] else o )
