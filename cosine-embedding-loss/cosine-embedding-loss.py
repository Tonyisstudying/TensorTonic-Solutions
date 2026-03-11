import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    x1, x2 = np.array(x1), np.array(x2)
    norm1, norm2 = np.linalg.norm(x1), np.linalg.norm(x2)
    dot = np.sum(x1*x2)
    cosine = dot / (norm1*norm2)
    if label == 1:
        loss = 1 - cosine
    else:
        loss = max(0,cosine - margin)
    return loss