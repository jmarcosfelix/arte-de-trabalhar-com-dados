import numpy as np


def frequencia_relativa(freq):
    result = []
    total = np.sum(freq)
    for f in freq:
        result.append(np.round(f / total * 100, 2))
    if np.sum(result) < 100.00:
        index = result.index(np.max(result))
        result[index] = result[index] + (100.00 - np.sum(result))
    return result
