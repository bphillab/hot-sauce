import numpy as np

def sample_gamma(n, mode=1.0, shape=5.0):
    scale = mode / (shape - 1)
    return np.random.gamma(shape=shape, scale=scale, size=n)

def remove_nones(lst):
    return [x for x in lst if x != None]
