import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    padded = np.full((len(seqs), max_len), pad_value)
    # step: fill each sequence
    for i,seq in enumerate(seqs):
        trunc = seq[:max_len]
        padded[i, :len(trunc)] = trunc
    return padded
    pass