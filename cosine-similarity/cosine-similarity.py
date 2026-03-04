import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    dot = np.dot(a,b)
    norm_a, norm_b = np.linalg.norm(a), np.linalg.norm(b)
    if norm_a ==0 or norm_b==0:
        return 0
    return dot / (norm_a * norm_b)
    pass