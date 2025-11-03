# Practical 8: Find the orthonormal basis of a given vector space using 
# the Gram-Schmidt orthogonalization process.

import numpy as np

def gram_schmidt(V):
    U = [] 
    
    for v_k in V:
        u_k = v_k.copy().astype(float)
        
        for u_j in U:
            projection = (np.dot(v_k, u_j) / np.dot(u_j, u_j)) * u_j
            u_k -= projection
            
        if np.linalg.norm(u_k) > 1e-10:
            U.append(u_k)
            
    E = []
    for u in U:
        e = u / np.linalg.norm(u)
        E.append(e)
        
    return U, E

# --- Define the initial set of vectors ---
v1 = np.array([1, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([2, 1, 2]) # v3 is linearly dependent

vectors = [v1, v2, v3]

print("--- Practical 8: Gram-Schmidt Orthogonalization ---")
print("Original set of vectors (V):")
for v in vectors:
    print(v)

orthogonal_basis, orthonormal_basis = gram_schmidt(vectors)

print("\n--- Orthogonal Basis (U) ---")
for u in orthogonal_basis:
    print(u)

print("\n--- Orthonormal Basis (E) ---")
for e in orthonormal_basis:
    print(e)

print("\n--- Verification: Dot Products of Orthonormal Basis ---")
e1 = orthonormal_basis[0]
e2 = orthonormal_basis[1]
print(f"e1 . e2 = {np.dot(e1, e2)}")