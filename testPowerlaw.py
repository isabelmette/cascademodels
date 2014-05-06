import v1; reload(v1)
import v2; reload(v2)
import numpy as np
import matplotlib.pyplot as plt

vals1 = [v2.samplepowerlaw(exponent=0.01, minval=1) for x in range(100000)]
vals2 = [v2.samplepowerlaw(exponent=0.10, minval=1) for x in range(100000)]
vals3 = [v2.samplepowerlaw(exponent=2.10, minval=1) for x in range(100000)]
vals4 = [v2.samplepowerlaw(exponent=3.20, minval=1) for x in range(100000)]

fig = plt.figure()
ax = fig.add_subplot(211)
ax.hist(vals1)
ax.hist(vals2)
ax = fig.add_subplot(212)
ax.hist(np.log10(vals3), log=True)
ax.hist(np.log10(vals4), log=True)
plt.savefig('temp.pdf')
