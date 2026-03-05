import numpy as np
import math

def gelu(x):
    x = np.array(x)
    return 0.5 * x * (1 + np.vectorize(math.erf)(x / np.sqrt(2)))
