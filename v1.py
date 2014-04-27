import numpy as np

def samplepowerlaw(exponent, minval):
    if minval <= 0:
        raise Exception("Retry with minval > 0.")

    e = exponent
    x = np.random.random()
    val = ((1. - x) * ((minval) **(1 - e)) )**(1./ (1. - e))
    return val

def fname(net):
    return "network_a="+ str(net.a)+ "_b="+ str(net.b)+ "_p="+ str(net.p) +  ",seed=" + str(net.seed) + ".dat"

class network:
    def __init__(self, a, b, p, seed):
        self.a = a
        self.b = b
        self.p = p
        self.seed = seed
        np.random.seed(seed)

        self.t0 = 1

        self.outfname = fname(self)

        self.nodes = []
        self.leaf_nodes = set()
        self.terminated_early = False # Assume false unless changed

        self.max_nodes = 1000000
        root = node(self, 0, 0, self.a, self.b, self.p, self.t0)

     
    def runtime(self, tnow, tmax, inc=1):
        for t in range(tnow, tmax, inc):
            self.t = t
            if self.leaf_nodes:
                for node in list(self.leaf_nodes):
                    if t >= node.tv:
                        node.add_children(self, t)
            else:
                self.terminated_early = True
                break
            
class node:
    def __init__(self, network, parent, depth, a, b, p, t0):
        self.parent = parent
        self.id = len(network.nodes)
        self.depth = depth
        network.nodes.append(self)
        network.leaf_nodes.add(self)
            
        self.a = a
        self.b = b
        self.p = p
        self.t0 = t0


        self.reshare = np.random.random() < self.p
        if self.reshare:
            dv = samplepowerlaw(exponent = self.a, minval=1)
            self.dv = int(np.floor(dv))
        else:
            self.dv = 0

        self.tv = samplepowerlaw(exponent = self.b, minval=self.t0)
   
    def add_children(self, network, t):
        network.leaf_nodes.remove(self)
        for ichild in range(self.dv):
            if len(network.nodes) >= network.max_nodes:
                self.terminated_early = True
                break
            node(network, self.id, self.depth+1, self.a, self.b, self.p, t0=t)


