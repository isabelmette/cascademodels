import networkx as nx
import matplotlib.pyplot as plt
import v1; reload(v1)
import numpy as np
from collections import Counter
net = v1.network(a=2, b=3, p=0.6)
tmax = 100
net.runtime(tnow=1, tmax=tmax)
if net.terminated_early:
    tmax = self.t
entertimes = [np.ceil(node.tv) for node in net.nodes]

outfile = datadir + "network.dat"



entertimecounts = Counter(entertimes)
cumulativetimecounts = np.zeros(tmax)
time = 1
cumulativetimecounts[time] = 0
for time in range(2, tmax):
    cumulativetimecounts[time] = entertimecounts[time] + cumulativetimecounts[time-1]

t2t = np.zeros(tmax/2)
for time in range(1, tmax/2):
    print time
    t2t[time] = cumulativetimecounts[2*time] / cumulativetimecounts[time]

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.hist(np.log10(entertimes), bins=100, log=True, cumulative=True)
#plt.savefig('cum_histentertimes.pdf')


fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(range(tmax/2), t2t)
plt.savefig('cum_histentertimes.pdf')


