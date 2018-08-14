import numpy as np

def sample_gamma(n, mode=1.0, shape=5.0):
    scale = mode / (shape - 1)
    return np.random.gamma(shape=shape, scale=scale, size=n)

def remove_nones(lst):
    return [x for x in lst if x != None]

def enum_to_data_frame(enum, list_of_enum_values):
    rows = [
        [(e in row) for e in enum]
        for row in list_of_enum_values]
    return pd.DataFrame(rows, columns=list(e.name for e in enum))
