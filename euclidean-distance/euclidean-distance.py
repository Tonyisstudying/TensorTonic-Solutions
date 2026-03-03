import math

def euclidean_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    res = 0
    if len(x) != len(y):
        raise ValueError
    for i in range(n):
        res += (x[i] - y[i])**2
    return math.sqrt(res)
        