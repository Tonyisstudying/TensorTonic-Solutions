import numpy as np
def bernoulli_pmf_and_moments(x, p):
    x = np.array(x)

    if not np.all((x==0)|(x==1)):
        raise ValueError
    if not (0.0 <= p <= 1.0):
        raise ValueError
    pmf = (p ** x) * ((1-p)**(1-x))
    mean = p
    var = p * (1 - p)
    return pmf, mean, var
     