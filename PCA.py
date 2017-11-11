import numpy as np
from scipy import linalg as LA

A = np.array([[1, 0.9, 0],
              [0, 1, 0],
              [0, 0.9, 1]])

print A

e_vals, e_vecs = LA.eig(A)

print e_vals
print e_vecs
