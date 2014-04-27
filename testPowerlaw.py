import v1; reload(v1)
import numpy as np
import matplotlib.pyplot as plt

vals = [v1.samplepowerlaw(1.j1, 1) for x in range(100000)]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(np.log10(vals), log=True)
plt.savefig('temp.pdf')
