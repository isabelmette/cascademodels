import networkx as nx
import matplotlib.pyplot as plt
import v1; reload(v1)
import numpy as np
net = v1.network(a=2, b=3, p=0.6)

net.runtime(tnow=1, tmax=7)

edges = [(node.parent, node.id) for node in net.nodes]
nodes = [node.id for node in net.nodes]
depths = [node.depth for node in net.nodes]
shells = [[] for depth in set(depths)]
for node, depth in zip(nodes, depths):
    shells[depth].append(node)

G = nx.Graph()
G.add_edges_from(edges)
fig = plt.figure()
ax =fig.add_subplot()
print 'getting layout'
pos = nx.graphviz_layout(G, prog='dot')

nx.draw_networkx(G, pos=pos, ax=ax)
plt.savefig('tempnet.pdf')
