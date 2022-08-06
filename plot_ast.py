import networkx as nx
from matplotlib import pyplot as plt

from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser


s = """
    x = fun(){ x = 1; };
    a = 1;
    """

# s = "x = 2 + 1;"

# s = "x = y = 1;"

# s = 'b = 1 == false ;'

# s = "b = (1 + 1);"

s = "1+2;"


p = Parser(TokenStream(CharStream(s)))
a = p.parse()[ (n := 0) ] # nth statement


pos =  {}
# v = (0,0)

def to_edgelist(ast:dict, p:str=None, ppos=(0,0)): # a: ast

    global pos

    a = ast
    el = []

    # tx represents the current node
    try:
        tx = a['type']+str(id(a)%100) # type + hierarchy id
    except:
        tx = None

    # these are tx's children
    try:
        cld = a.keys() # children
    except:
        cld = []

    
    if tx not in pos   and tx is not None :
        if 'left' in tx:
            pos[tx] = (ppos[0]-1, ppos[1]-1) # down and to the left
        else:
            pos[tx] = (ppos[0]+1, ppos[1]-1) # down and to the right


    if tx is not None:
        if p is not None: # p is tx's parent
            el+=[(p, tx)]
        
        u = [c+str(id(a)%100) for c in cld if c!='type']
        el+=[(tx, i) for i in u ]

    
    if len(cld) > 0:
        for i, c in enumerate(cld):
            
            cx = c+str(id(a)%100) # child + hierarchy id


            if cx not in pos:
                print(c, "hello there")
                y = pos[tx][1] -1 # tx is cx's parent
                if 'left' in cx:
                    pos[cx] = (pos[tx][0]-1, y)
                else:
                    pos[cx] = (pos[tx][0]+1, y)

            
            el += to_edgelist(a[c], cx, pos[cx])
    
    return el


el = to_edgelist(a)
print(el, "\n")

print(pos)


coord = pos
g = nx.from_edgelist(el)
nx.draw(g, with_labels=True, node_size=1500, node_color="skyblue", pos=coord) 
plt.show()
