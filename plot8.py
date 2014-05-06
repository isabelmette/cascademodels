import networkx as nx
import matplotlib.pyplot as plt
import v1; reload(v1)
import pandas as pd
import numpy as np

datadir = "data/"
tmax = 10000
fname = datadir + "network_a=binarytree_b=2.0_p=0.7,seed=944555.dat"
fname = datadir + "network_a=binarytree_b=0.01_p=1.0,seed=103737.dat"

data = pd.read_table(fname, skiprows=2, usecols=[0, 1, 2, 3], delimiter=' ', names=['u', 'v', 'r', 't'])
u = data['u']
v = data['v']
r = data['r']
t = data['t']

G = nx.Graph()
resharetimes = np.ceil(t[r>0])

us = u
vs = v
edges = zip(us, vs)

foo = t < tmax
foo2 = r > 0 

G.add_edges_from(edges)
pos = nx.graphviz_layout(G, prog='dot')
nodecolor = ['b' if re else 'r' for re in r]
nodesize = [75 if te < tmax else 40 for te in t]
fig = plt.figure()
ax =fig.add_subplot()


nx.draw_networkx(G, pos=pos, ax=ax, with_labels=False, node_size=nodesize, node_color=nodecolor)
plt.savefig('tempnet.pdf')

