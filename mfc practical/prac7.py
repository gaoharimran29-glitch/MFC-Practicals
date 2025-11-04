# Practical 7: 
# 1. Check the linear dependence of vectors.
# 2. Generate a linear combination of given vectors.
# 3. Find the transition matrix of given matrix space.

import numpy as np
from sympy import Matrix

# --- Part 1: Check Linear Dependence of Vectors ---
print("--- Part 1: Linear Dependence Check ---")

# Example 1: Linearly Independent Vectors
vec1 = [1, 0, 0]
vec2 = [0, 1, 1]
vec3 = [1, 0, 1]
vectors_ind = Matrix([vec1, vec2, vec3]).transpose()
rank_ind = vectors_ind.rank()

print(f"Vectors: {vec1}, {vec2}, {vec3}")
print(f"Matrix:\n{vectors_ind}")
print(f"Rank: {rank_ind}, Number of Vectors: 3")
if rank_ind == 3:
    print("Result: The vectors are linearly INDEPENDENT.\n")
else:
    print("Result: The vectors are linearly DEPENDENT.\n")

# Example 2: Linearly Dependent Vectors
vec4 = [1, 2, 3]
vec5 = [4, 5, 6]
vec6 = [5, 7, 9]  # vec6 = vec4 + vec5
vectors_dep = Matrix([vec4, vec5, vec6]).transpose()
rank_dep = vectors_dep.rank()

print(f"Vectors: {vec4}, {vec5}, {vec6}")
print(f"Matrix:\n{vectors_dep}")
print(f"Rank: {rank_dep}, Number of Vectors: 3")
if rank_dep == 3:
    print("Result: The vectors are linearly INDEPENDENT.\n")
else:
    print("Result: The vectors are linearly DEPENDENT.\n")


# --- Part 2: Generate a Linear Combination of Vectors ---
print("--- Part 2: Linear Combination ---")
v1 = np.array([1, 5])
v2 = np.array([-2, 3])
c1 = 10
c2 = -3
linear_combination = (c1 * v1) + (c2 * v2)

print(f"v1 = {v1}, v2 = {v2}")
print(f"c1 = {c1}, c2 = {c2}")
print(f"Linear Combination (c1*v1 + c2*v2) = {linear_combination}\n")


# --- Part 3: Find the Transition Matrix ---
# The formula is P = C_inv * B
print("--- Part 3: Transition Matrix ---")

# Basis B vectors
b1 = [1, 1]
b2 = [2, 0]
# Matrix with B vectors as columns
B_matrix = Matrix([b1, b2]).transpose()
print(f"Basis B matrix:\n{B_matrix}")

# Basis C vectors
c1 = [1, -1]
c2 = [1, 1]
# Matrix with C vectors as columns
C_matrix = Matrix([c1, c2]).transpose()
print(f"Basis C matrix:\n{C_matrix}")

# 1. Find the inverse of C
C_inv = C_matrix.inv()
print(f"Inverse of C matrix:\n{C_inv}")

# 2. Calculate P = C_inv * B
P_transition_B_to_C = C_inv * B_matrix

print("\nTransition Matrix from B to C (P = C_inv * B):")
print(P_transition_B_to_C)