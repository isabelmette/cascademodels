import networkx as nx
import pandas as pd
import time
import matplotlib.pyplot as plt
import v1; reload(v1)
import numpy as np
from collections import Counter
import glob

datadir = "data/"
infnames = glob.glob(datadir + "network_*.dat")
networks = []
resharetimes = []
for fname in infnames:
    picname = fname.replace('data', 'pics')
    
    t1 = time.time()
    data = pd.read_table(fname, skiprows=2, usecols=[2, 3], delimiter=' ', names=['r', 't'])
    r = data['r']
    t = data['t']
    t2 = time.time()
    resharetimes = np.ceil(t[r>0]).astype(int)

    resharetimecounts = Counter(resharetimes)
    t3 = time.time()
    tmax = max(resharetimes)
    cumulativetimecounts = np.zeros(tmax)
    t = 1
    cumulativetimecounts[t] = 0
    for t in range(2, tmax):
        cumulativetimecounts[t] = resharetimecounts[t] + cumulativetimecounts[t-1]
    t4 = time.time()

    t2t = np.zeros(tmax/2)
    for t in range(2, tmax/2):
        t2t[t] = cumulativetimecounts[2*t] / cumulativetimecounts[t]
    t5 = time.time()

    picname = picname.replace('.dat', '_histsReshareTimes.pdf')
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.hist(np.log10(resharetimes), bins=100, log=True, cumulative=False)
    ax.set_xlabel('log reshare time')
    ax.set_ylabel('count')

    ax = fig.add_subplot(212)
    ax.loglog(range(tmax/2), t2t)
    ax.set_xlabel('log reshare time')
    ax.set_ylabel('count 2 * now / count now ')
    plt.savefig(picname)


    print t2- t1
    print t3- t2
    print t4- t3
    print t5- t4
