import networkx as nx
from matplotlib import pyplot as plt
import re

from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser



def get_cpos(cx:str, ppos:(int, int))->(int, int): # child's pos from parent's pos

    y_dwn = ppos[1]-1

    if 'left' in cx:
        return (ppos[0]-1, y_dwn) # down and to the left
    if 'right' in cx:
        return (ppos[0]+1, y_dwn) # down and to the right

    return (ppos[0], y_dwn) # down 


def to_edgelist(ast:dict, p:str=None, ppos=(0,1)): # p: parent, ppos: parent's position

    pos = {} # node : position 
    el = [] # edge list
    hier_id = str(id(ast)) # hierarchy id
    labels = {}

    if not isinstance(ast, dict): # base case
        return el, pos, {p : ast}
    
    tx = ast['type']+hier_id # current node
    cld = [c for c in ast.keys() if c != 'type'] # current node's children

    labels.update({tx : ast['type']})
    labels.update({ c+hier_id: c for c in cld })
    
    if p is not None: # p is tx's parent
        el+=[(p, tx)]

    pos[tx] = get_cpos(tx, ppos) # tx's position as a func of parent's

    el+=[ (tx, c+hier_id) for c in cld ]
    pos.update( {c+hier_id : get_cpos(c+hier_id, pos[tx]) for c in cld } )

    for c in cld:
        _el, _pos, _labels = to_edgelist(ast[c], c+hier_id, pos[c+hier_id])
        el+=_el
        pos.update(_pos)
        labels.update(_labels)
    
    return el, pos, labels
    

def plot_ast(ast:dict):

    el, pos, labels = to_edgelist(ast)
    g = nx.from_edgelist(el)
    nx.draw(g, with_labels=False, node_size=1500, node_color="skyblue", pos=pos) 
    nx.draw_networkx_labels(g, pos, labels ,font_size=16,font_color='k')
    plt.show()


def main():
    s = """
    x = fun(){ x = 1; };
    a = 1;
    """
   
    # s = "f(1);" 
    # s = "x = y = z = 1;" # wrong
    # s = "true+false;" # problem!
    # s = "x = y =  1;" 
    # s = 'b = 1 == false ;'
    # s = "b = (1 + 1);"
    # s = "b = (1 + (2+3));"
    # s = "b = (1 +  (x = 1));"
    # s = "a=1;"
    # s = "x = true || false;"
    s = "x = 2 + 1;"
    s = "1+2*4;"
    s = "1+2;"
    

    p = Parser(TokenStream(CharStream(s)))
    a = p.parse()[ (n := 0) ] # nth statement
    plot_ast(a)


if __name__ == '__main__':
    main()