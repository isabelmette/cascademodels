import numpy as np
basedatadir = "data/"
basepicdir = "pics/"
runtag = 'testing'
datadir = basedatadir + runtag + "/"
picdir = basepicdir + runtag + "/"

bs = [0.01, 0.1, 0.5, 1.1, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0]
ps = np.linspace(0.1, 1, num=11)
a = 'binarytree'

nruns = 1000
tmax = 200
