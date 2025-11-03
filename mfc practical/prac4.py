# Practical 4: Solve a system of Homogeneous and non-homogeneous equations 
# using Gauss elimination method.

import numpy as np

# Coefficient Matrix (A) Elements
# A 3x3 matrix for a system of 3 equations with 3 variables
Coefficient_Matrix = np.array([[2, 1, -1],
                               [-3, -1, 2],
                               [-2, 1, 2]], dtype=float)

print("Coefficient Matrix (A) is as follows:", '\n', Coefficient_Matrix, '\n')

# Column Matrix (B) Elements
# A 3x1 matrix for the constants
Column_Matrix = np.array([[8],
                          [-11],
                          [-3]], dtype=float)

print("Column Matrix (B) is as follows:", '\n', Column_Matrix, '\n')

# Solution of the system of Equations using Gauss elimination method
# np.linalg.solve(A, B) solves the system AX = B for X
Solution_of_the_system_of_Equations = np.linalg.solve(Coefficient_Matrix, Column_Matrix)

print("Solution of the system of Equations (X) using Gauss elimination method:")
print(Solution_of_the_system_of_Equations)