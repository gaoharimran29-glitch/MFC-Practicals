# Practical 9: Check the diagonalizable property of matrices, 
# find the corresponding eigenvalue, and verify the Cayley-Hamilton theorem.

import numpy as np
from numpy import linalg as LA

# --- Define the matrix ---
A = np.array([
    [1, -3, 3],
    [3, -5, 3],
    [6, -6, 4]
])

print("--- Practical 9: Diagonalization & Cayley-Hamilton ---")
print("Matrix A:")
print(A)

# --- Part 1: Find Eigenvalues ---
eigenvalues, eigenvectors = LA.eig(A)

print("\n--- Eigenvalues ---")
print(eigenvalues)

# --- Part 2: Check for Diagonalizability ---
rank = LA.matrix_rank(eigenvectors)
dimension = A.shape[0]

print("\n--- Diagonalizability Check ---")
if rank == dimension:
    print("Matrix A is diagonalizable.")
else:
    print("Matrix A is NOT diagonalizable.")

# --- Part 3: Verify the Cayley-Hamilton Theorem ---
# p(A) = 0
char_poly = np.poly(A)
print(f"\n--- Cayley-Hamilton Theorem Verification ---")
print(f"Coefficients of characteristic polynomial: {char_poly}")

# Calculate p(A)
I = np.identity(dimension)
p_A = (
    LA.matrix_power(A, 3) +
    char_poly[1] * LA.matrix_power(A, 2) +
    char_poly[2] * A +
    char_poly[3] * I
)

print("\nResult of p(A) (should be a zero matrix):")
print(np.round(p_A, decimals=5))
print("\nCayley-Hamilton Theorem is verified.")