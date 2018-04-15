"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

x = scores
print(np.exp(x))
print(np.sum(np.exp(x), axis=0))