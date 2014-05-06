import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data/data.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(data[:, 0], data[:, 1])
plt.savefig('data.pdf')
