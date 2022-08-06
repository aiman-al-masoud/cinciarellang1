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


pos =  {}
v = (0,0)

def to_edgelist(ast:dict, p:str=None): # a: ast

    global pos

    a = ast
    el = []

    try:
        cld = a.keys() # children
    except:
        cld = []
    
    try:
        tx = a['type']+str(id(a)%100) # type + hierarchy id
    except:
        tx = None
    
    if tx not in pos:
        pos[tx] =  v

    if tx is not None:
        if p is not None:
            el+=[(p, tx)]
        
        u = [c+str(id(a)%100) for c in cld if c!='type']
        el+=[(tx, i) for i in u ]

    
    if len(cld) > 0:
        for i, c in enumerate(cld):
            el += to_edgelist(a[c], c+str(id(a)%100))

            if c+str(id(a)%100) not in pos:
                print(c, "hello there")
                y = v[1] -1
                if 'left' in c+str(id(a)%100):
                    pos[c+str(id(a)%100)] = (v[0]-1, y)
                else:
                    pos[c+str(id(a)%100)] = (v[0]+1, y)
    
    return el


el = to_edgelist(a)
print(el, "\n")

print(pos)


# from random import randint
# # lvl = 0
# def get_coord(n: str):
#     import re 
#     l = int(re.sub('\D+', '', n))
#     return (randint(1, 10), l)
# coord = {  n : get_coord(n)  for n in [e[0] for e in el]+[e[1] for e in el] }
# print(coord)

coord = pos
g = nx.from_edgelist(el)
nx.draw(g, with_labels=True, node_size=1500, node_color="skyblue")#, pos=coord) 
plt.show()
