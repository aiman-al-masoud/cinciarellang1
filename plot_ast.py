import networkx as nx
from matplotlib import pyplot as plt

from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser


s = """
    x = fun(){ x = 1; };
    a = 1;
    """

s = "x = 2 + 1;"

s = "x = y = 1;"

s = 'b = 1 == false ;'

s = "b = (1 + 1);"

s = "1+2;"


p = Parser(TokenStream(CharStream(s)))
a = p.parse()[ (n := 0) ] # nth statement


def to_edgelist(ast:dict, p:str=None): # a: ast

    a = ast
    el = []

    try:
        cld = a.keys() # children
    except:
        cld = []
    
    try:
        xc = a['type']+str(id(a)%100)
    except:
        xc = None

    if xc is not None:
        if p is not None:
            el+=[(p, xc)]
        
        u = [c+str(id(a)%100) for c in cld if c!='type']
        el+=[(xc, i) for i in u ]

    
    if len(cld) > 0:
        for c in cld:
            el += to_edgelist(a[c], c+str(id(a)%100))
    
    return el


el = to_edgelist(a)
print(el)


# from random import randint
# # lvl = 0
# def get_coord(n: str):
#     import re 
#     l = int(re.sub('\D+', '', n))
#     return (randint(1, 10), l)
# coord = {  n : get_coord(n)  for n in [e[0] for e in el]+[e[1] for e in el] }
# print(coord)

g = nx.from_edgelist(el)
nx.draw(g, with_labels=True, node_size=1500, node_color="skyblue")#, pos=coord) 
plt.show()
