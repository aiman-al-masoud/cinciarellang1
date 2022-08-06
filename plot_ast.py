import networkx as nx
from matplotlib import pyplot as plt
import re

from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser


s = """
    x = fun(){ x = 1; };
    a = 1;
    """

# s = "x = 2 + 1;"

s = "x = y = z = 1;" # wrong
 
s = "x = y =  1;" 

s = 'b = 1 == false ;'

s = "b = (1 + 1);"

# s = "1+2;"

# s = "a=1;"

# s = "true+false;" # problem!

s = "x = true || false;"



p = Parser(TokenStream(CharStream(s)))
a = p.parse()[ (n := 0) ] # nth statement



def to_edgelist(ast:dict): # a: ast

    pos = {}

    def get_cpos(cx:str, ppos:(int, int)): # child's pos from parent's pos

        y_dwn = ppos[1]-1

        if 'left' in cx:
            return (ppos[0]-1, y_dwn) # down and to the left
        if 'right' in cx:
            return (ppos[0]+1, y_dwn) # down and to the right

        return (ppos[0], y_dwn) # down 
    

    def inner(ast:dict, p:str=None, ppos=(0,1)): # p: parent, ppos: parent's position
        
        nonlocal pos
        a = ast
        el = []
        hier_id = str(id(a)) # hierarchy id

        if not isinstance(a, dict):
            return el
        
        tx = a['type']+hier_id # type + hierarchy id
        cld = [c for c in a.keys() if c != 'type'] # children

        # if tx not in pos:
        pos[tx] = get_cpos(tx, ppos)
        # else:
            # print("I was gonna get added again")
        
        if p is not None: # p is tx's parent
            el+=[(p, tx)]
        else:
            print("I was gonna get added again!")

            
        el+=[ (tx, c+hier_id) for c in cld ]


        if len(cld) > 0:
            for c in cld:
                
                cx = c+hier_id # child + hierarchy id

                # if cx not in pos:
                pos[cx] = get_cpos(cx, pos[tx])
                # else:
                    # print("I was gonna get added again!")

                el += inner(a[c], cx, pos[cx])
        
        return el

    return inner(ast), pos


def plot_ast(ast:dict):

    el, pos = to_edgelist(ast)
    # print(el, "\n", pos)
    g = nx.from_edgelist(el)
    nx.draw(g, with_labels=False, node_size=1500, node_color="skyblue", pos=pos) 
    labels  = {p[0]:re.sub('\d+', '', p[0]) for p in pos.items() if 'type' not in p[0]}
    nx.draw_networkx_labels(g, pos, labels ,font_size=16,font_color='k')
    plt.show()

plot_ast(a)
