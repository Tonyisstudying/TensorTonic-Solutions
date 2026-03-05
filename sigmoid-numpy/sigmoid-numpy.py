import numpy as np

def sigmoid(x):
    x = np.array(x)
    res = 1/(1+np.e**(-x))
    return res
    pass