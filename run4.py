import networkx as nx
import os
import matplotlib.pyplot as plt
import v2; reload(v2)
import numpy as np
import time
from collections import Counter
import params1 as S; reload(S)

try:
    os.system("mkdir " + S.basedatadir + S.runtag)
except:
    os.system("rm " + S.basedatadir + S.runtag + "/*")

datadir = S.basedatadir + S.runtag + "/"


for p in S.ps:
    for b in S.bs:
        for run in range(S.nruns):
            seed = int(time.time() * 1000000 - int(time.time())*1000000)
            net = v2.network(b=b, p=p, seed=seed)
            net.runtime(tnow=1, tmax=S.tmax)

            outf = open(datadir + net.outfname, 'w')
            outf.writelines("tmax=" + str(S.tmax) + "_terminatedEarly=" + str(net.terminated_early) + "\n" )
            outf.writelines("u v t_v\n")

            for node in net.nodes:
                u = node.parent.id
                v = node.id
                t = node.tv
                r = int(node.reshare)
                line = " ".join([str(u), str(v), str(r), str(t)])
                outf.writelines(line + "\n")
                
            outf.close()
