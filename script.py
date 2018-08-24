import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#import igraph

def ldata(archive):
	f=open(archive)
	data=[]
	for line in f:
		line=line.strip()
		col=line.split()
		data.append(col)	
	return data

data=ldata('yeast_Y2H.txt')
#print(data)

#G = nx.Graph()
G=nx.read_edgelist('yeast_Y2H.txt')
nodos=G.number_of_nodes()
edges=G.number_of_edges()
print(nodos)
print(edges)

medio=0.0

for i in range(0,nodos):
	medio+=list(G.degree)[i][1]

medio = medio / nodos

#densidad = palitos observados / palitos posibles max

densidad = edges / (nodos*(nodos-1))

#G.add_node(1)#agrego un nodo
#for i in data:
#	G.add_nodes_from(i)#una lsita de nodos

'''
G.add_edge(1,2)
e = (1,2)
G.add_edge(*e)#*lista o *tupla desempaqueta el objeto
G.add_edges_from([(1,2), (1,3)])
G = nx.Graph()#directed

G.add_edges_from([(1, 2), (2, 3), (3, 1)])
'''
#nx.draw(G, with_labels=False, font_weight='bold',node_size=40)
#plt.show()


'''

G = nx.Graph()

G.add_node(1)#agrego un nodo
G.add_nodes_from([2,3])#una lsita de nodos

G.add_edge(1,2)
e = (1,2)
G.add_edge(*e)#*lista o *tupla desempaqueta el objeto
G.add_edges_from([(1,2), (1,3)])
G = nx.Graph()#directed

G.add_edges_from([(1, 2), (2, 3), (3, 1)])
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
'''