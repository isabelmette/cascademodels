import networkx as nx
import matplotlib.pyplot as plt
import v1; reload(v1)
import numpy as np
import time
from collections import Counter
tmax = 100

datadir = "data/"
a = 2
b = 3
p = 0.6
nruns = 100
seeds = np.loadtxt('100seeds.dat', dtype=int)
for run, seed in enumerate(seeds):
    net = v1.network(a=2, b=3, p=0.6, seed=seed)
    net.runtime(tnow=1, tmax=tmax)
    if net.terminated_early:
        tmax = net.t

    outf = open(datadir + net.outfname, 'w')
    outf.writelines("tmax=" + str(tmax) + "_terminatedEarly=" + str(net.terminated_early) + "\n" )
    outf.writelines("u v r t_v\n")

    for node in net.nodes:
        u = node.parent
        v = node.id
        t = node.tv
        r = int(node.reshare)
        line = " ".join([str(u), str(v), str(r), str(t)])
        outf.writelines(line + "\n")
        
    outf.close()
