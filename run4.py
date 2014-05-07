import networkx as nx
import itertools
from sklearn.externals.joblib import Parallel, delayed
import os
import matplotlib.pyplot as plt
import v2; reload(v2)
import numpy as np
import time
from collections import Counter
import params1 as S; reload(S)
#from VeryPicklableObject import *

try:
    os.system("mkdir " + S.basedatadir + S.runtag)
except:
    os.system("rm " + S.basedatadir + S.runtag + "/*")

combs = list(itertools.product(S.bs, S.ps, range(S.nruns)))


#@picklableInstancemethod
def funcrun(b, p, run, S):
    seed = int(time.time() * 1000000 - int(time.time())*1000000)
    net = v2.network(b=b, p=p, seed=seed)
    net.runtime(tnow=1, tmax=S.tmax)

    outf = open(S.datadir + net.outfname, 'w')
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
Parallel(n_jobs=1, verbose=2)(delayed(funcrun)(b, p, run, S) for b, p, run in combs)
