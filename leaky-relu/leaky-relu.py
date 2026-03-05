import numpy as np

def leaky_relu(x, alpha=0.01):
    x = np.array(x)
    return x * np.where(x < 0,alpha, 1)