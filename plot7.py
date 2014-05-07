
import networkx as nx
import os
import pandas as pd
import time
import matplotlib.pyplot as plt
import v1; reload(v1)
import numpy as np
from collections import Counter
import glob


networks = []
resharetimes = []

import params1 as S; reload(S)
try:
    os.system("mkdir " + S.basepicdir + S.runtag)
except:
    print S.picdir, 'already exists.'

# PLOT cumulative number shared as function of p and b in params file

for ip, p in enumerate(S.ps):
    nplots = len(S.bs)
    fig = plt.figure(figsize=(6, 3 * nplots))
    for ib, b in enumerate(S.bs):
        infnames = glob.glob(S.datadir + "network_*" + str(S.a) + "*" + str(b) + "*" + str(p) + "*.dat")[:S.nruns]
        reshareevents = np.zeros((S.nruns, S.tmax))
        cumulativere = np.zeros((S.nruns, S.tmax))

        for irun, fname in enumerate(infnames):

            data = pd.read_table(fname, skiprows=2, usecols=[2, 3], delimiter=' ', names=['r', 't'])
            r = data['r']
            t = data['t']

            resharetimes = np.ceil(t[r>0])
            numtimes = Counter(resharetimes[resharetimes < S.tmax])
            for time, num in numtimes.items():
                reshareevents[irun, time] += num
        cumulativere = reshareevents.cumsum(axis=1)
        meancum = np.mean(cumulativere, axis=0)
        stdecum = np.std(cumulativere, axis=0)/np.sqrt(S.nruns)
 
        ax = fig.add_subplot(nplots, 1, ib+1)
        print fname, p, fname
        ax.set_title('p='+ str(p) + ' b=' + str(b))
        ax.fill_between(range(S.tmax), meancum-stdecum, meancum+stdecum, alpha=0.5)

    pname = fname.split('p=')[0].replace('data', 'pics') + '_cumMeanReshares.pdf'
    plt.savefig(pname)
