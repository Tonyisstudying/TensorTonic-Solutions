import numpy as np

def swish(x):
    x= np.array(x)
    sigmoid = 1 / (1 + np.e**(-x))
    return x*sigmoid