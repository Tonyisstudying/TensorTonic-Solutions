import numpy as np

def expected_value_discrete(x, p):
    x, p = np.array(x), np.array(p) 
    if np.sum(p) != 1:
        raise ValueError
    return np.sum(x*p)
