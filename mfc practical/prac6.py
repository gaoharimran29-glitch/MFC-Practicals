import numpy as np
from sympy import Matrix

# Define a new matrix
A_np = np.array([[1, 2, 0, 4],
                 [2, 4, 1, 3],
                 [3, 6, 1, 7]], dtype=float)

# Convert to a sympy Matrix
A = Matrix(A_np)
print("Matrix (A) is as follows:", '\n', A, '\n')

# Null Space & Nullity
print("--- Null Space & Nullity ---")

# Find the basis for the Null Space
null_space = A.nullspace()
print("Basis for Null Space:", null_space)

# Find the Rank (needed for Nullity)
rank = A.rank()
print("Rank of A:", rank)

# Nullity = Number of Columns - Rank
num_cols = A.shape[1]
nullity = num_cols - rank
print("Nullity of A:", nullity, '\n')

# Column Space
print("--- Column Space ---")
col_space = A.columnspace()
print("Basis for Column Space:", col_space, '\n')

# Row Space
print("--- Row Space ---")
row_space = A.rowspace()
print("Basis for Row Space:", row_space, '\n')

# This is the Null Space of the Transpose of A (A^T)
print("--- Left Null Space (Null Space of A^T) ---")
A_T = A.transpose()
print("Transpose of A (A^T) is:", '\n', A_T, '\n')

left_null_space = A_T.nullspace()
print("Basis for Left Null Space:", left_null_space)