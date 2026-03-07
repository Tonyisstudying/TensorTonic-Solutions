import numpy as np

def elu(x, alpha):
    x = np.array(x)
    res = np.where(x>0, x, alpha*(np.e**x - 1))
    return res.tolist()