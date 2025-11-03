# Practical 5: Solve a system of Homogeneous equations using the Gauss Jordan method.
# Implementing this method by calculating X = inv(A) * B

import numpy as np
from numpy import linalg

# Coefficient Matrix (A) Elements
Coefficient_Matrix = np.array([[2, 1, -1],
                               [-3, -1, 2],
                               [-2, 1, 2]], dtype=float)

print("Coefficient Matrix (A) is as follows:", '\n', Coefficient_Matrix, '\n')

# Column Matrix (B) Elements
Column_Matrix = np.array([[8],
                          [-11],
                          [-3]], dtype=float)

print("Column Matrix (B) is as follows:", '\n', Column_Matrix, '\n')

# Solution of Homogeneous System of Equations using GAUSS JORDAN Method:
# 1. Find the inverse of the coefficient matrix
Inv_of_Coefficient_Matrix = linalg.inv(Coefficient_Matrix)

print("Inverse of Coefficient Matrix (A⁻¹) is:", '\n', Inv_of_Coefficient_Matrix, '\n')

# 2. Multiply the inverse by the column matrix (X = A⁻¹B)
Solution_of_the_system_of_Equations = np.matmul(Inv_of_Coefficient_Matrix, Column_Matrix)

print("Solution of the system of Equations (X) using GAUSS JORDAN:")
print(Solution_of_the_system_of_Equations)