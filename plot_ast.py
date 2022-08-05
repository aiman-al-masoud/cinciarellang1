import networkx as nx
from matplotlib import pyplot as plt
from char_stream import CharStream
from token_stream import TokenStream
from parser import Parser


# s = "scemo = 1;"

s='x = fun(){ x = 1; }; a = 1;'
p = Parser(TokenStream(CharStream(s)))
a = p.parse()[0]

print(a)


# a = nx.from_dict_of_dicts( {0:  {1: {2: 0 }},  1 :  {2: {}}, 2 :{3: {}}  } )


# print(a)

# labels = nx.get_node_attributes(a, 'name')
# nx.draw(a, labels=labels)
# plt.show()

