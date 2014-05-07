
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

fig = plt.figure(figsize=(6, 5))
reshareevents = np.zeros((S.nruns, len(S.bs)))
cumulativere = np.zeros((S.nruns, len(S.bs)))
p = 1.0
for ib, b in enumerate(S.bs):
    infnames = glob.glob(S.datadir + "network_*" + str(S.a) + "*" + str(b) + "*" + str(p) + "*.dat")[:S.nruns]

    for irun, fname in enumerate(infnames):

        data = pd.read_table(fname, skiprows=2, usecols=[2, 3], delimiter=' ', names=['r', 't'])
        r = data['r']
        t = data['t']

        resharetimes = np.ceil(t[r>0])
        numtimes = Counter(resharetimes[resharetimes < S.tmax])
        reshareevents[irun, ib] += numtimes[2.] + numtimes[1.]
meancum = np.mean(reshareevents, axis=0)
stdecum = np.std(reshareevents, axis=0)/np.sqrt(S.nruns)
ax = fig.add_subplot(111)
#ax.set_title('p='+ str(p) + ' b=' + str(b))
ax.fill_between(range(S.tmax), meancum-stdecum, meancum+stdecum, alpha=0.6)

pname = fname.split('b=')[0].replace('data', 'pics') + '_reshareFnBeta.pdf'
plt.savefig(pname)
