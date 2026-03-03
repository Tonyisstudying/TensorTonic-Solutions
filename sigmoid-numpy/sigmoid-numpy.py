import numpy as np

def sigmoid(x):
    x = np.array(x)
    return np.where(
        x>=0,
        1 / (1+np.exp(-x)),
        #np.where(condition, value_if_true, value_if_false)
        np.exp(x) / (1+np.exp(x))
    )