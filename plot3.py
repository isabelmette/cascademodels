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

    data = pd.read_table(fname, skiprows=2, usecols=[2, 3], delimiter=' ', names=['r', 't'])
    r = data['r']
    t = data['t']
    tmax = 100
    
    resharetimes = np.ceil(t[r>0]).astype(int)
    resharetimes = resharetimes[resharetimes < tmax]
    if not resharetimes.any():
        continue
    if len(resharetimes) < 5:
        continue
    resharetimecounts = Counter(resharetimes)
    tmax = max(resharetimes)
    cumulativetimecounts = np.zeros(tmax)
    t = 0
    cumulativetimecounts[t] = 1
    
    for t in range(1, tmax):
        cumulativetimecounts[t] = resharetimecounts[t] + cumulativetimecounts[t-1]

    t2t = np.zeros(tmax/2)
    for t in range(tmax/2):
        t2t[t] = cumulativetimecounts[2*t] / cumulativetimecounts[t]
    
    picname = picname.replace('.dat', '_histsReshareTimes.pdf')
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.hist(np.log10(resharetimes), bins=100, log=True, cumulative=False)
    ax.set_xlim([0, 2])
    ax.set_ylim([0.1, 100000])
    ax.set_xlabel('log reshare time')
    ax.set_ylabel('count')

    ax = fig.add_subplot(212)
    ax.loglog(range(1, 1+tmax/2), t2t)
    ax.set_xlim([1, 100])
    ax.set_ylim([1, 100])
    ax.set_xlabel('log reshare time')
    ax.set_ylabel('count 2 * now / count now ')
    plt.savefig(picname)

