import pydot
from networkx.drawing.nx_pydot import graphviz_layout

import networkx as nx
from matplotlib import pyplot as plt



from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser

# s = "scemo = 1;"

s = """
    x = fun(){ x = 1; };
    a = 1;
    """

s = "x = 2 + 1;"

s = "x = y = 1;"

s = 'b = 1 == false ;'

s = "b = (1 + 1);"


p = Parser(TokenStream(CharStream(s)))
a = p.parse()[ (n := 0) ] # nth statement

# print(a)
# exit()




# a = nx.from_dict_of_dicts( {0:  {1: {2: 0 }},  1 :  {2: {}}, 2 :{3: {}}  } )


# print(a)

# labels = nx.get_node_attributes(a, 'name')
# nx.draw(a, labels=labels)
# plt.show()


# b = nx.from_edgelist([  (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)  ])
# # b = nx.from_nested_tuple(  ( )  , sensible_relabeling=True)

# lay = graphviz_layout(b, prog="circo")
# nx.draw(b, lay)
# plt.show()



# import networkx as nx
# import matplotlib.pyplot as plt
# # coord = {0: [8, 0], 2: [9, -1], 1: [8, -2], 4: [10, -2], 3: [9, -3], 5: [11, -3]}
# coord = {0: [8, 0], 2: [7, -1], 1: [8, -2], 4: [10, -2], 3: [9, -3], 5: [11, -3]}

# eg = [[0, 2], [2, 1], [2, 4], [4, 3], [4, 5]]
# g=nx.Graph()
# g.add_edges_from(eg) 
# nx.draw(g, with_labels=True, node_size=1500, node_color="skyblue", pos=coord) 
# plt.show()



# print(a)
# exit()


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


