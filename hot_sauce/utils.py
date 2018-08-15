import numpy as np
import pandas as pd


def sample_gamma(n, mode=1.0, shape=5.0):
    scale = mode / (shape - 1)
    return np.random.gamma(shape=shape, scale=scale, size=n)

def sample_beta_green(n):
    return np.random.beta(a=10.0, b=2.5, size=1)

def sample_beta_red(n):
    return np.random.beta(a=2.5, b=10.0, size=1)

def remove_nones(lst):
    return [x for x in lst if x != None]

def enum_to_data_frame(enum, list_of_enum_values):
    rows = [
        [(e in row) for e in enum]
        for row in list_of_enum_values]
    return pd.DataFrame(rows, columns=list(e.name for e in enum))
