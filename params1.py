import numpy as np
basedatadir = "data/"
basepicdir = "pics/"
runtag = 'testing'
datadir = basedatadir + runtag + "/"
picdir = basepicdir + runtag + "/"

bs = [1.11, 1.5, 1.7, 1.9, 2.0, 2.1, 2.2]
bs = [1.1001, 1.11, 1.5]
bs = np.linspace(1.1, 1.5, num=15)
ps = [1.0]
a = 'binarytree'

nruns = 500
tmax = 40
