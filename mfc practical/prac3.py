# PRACTICAL 3: FIND COFACTORS, DETERMINANT, ADJOINT AND INVERSE OF A MATRIX.

import numpy as np

A = np.array([[1, 2, 3],
              [0, 9, 5],
              [1, 0, 7]])

print("Matrix A is as follows:", '\n', A)

# For finding the Determinant a Matrix
Determinant_of_A = np.linalg.det(A)
print("\nThe Determinant of a Matrix is:", '\n', Determinant_of_A)

# For finding the Inverse of a Matrix
A_Inverse = np.linalg.inv(A)
print("\nThe Inverse of a Matrix is:", '\n', A_Inverse)

# cofactor(A) = (A_inverse)^T * det(A)
Transpose_of_A_Inverse = np.transpose(A_Inverse)

# Cofactor = transpose(A_inv) * det(A)
Cofactor_of_A = Transpose_of_A_Inverse * Determinant_of_A
print("\nThe Cofactor of a Matrix is:", '\n', Cofactor_of_A)

# For finding the Adjoint of a Matrix
# Adjoint(A) = transpose(Cofactor(A))
Adjoint_of_A = np.transpose(Cofactor_of_A)
print("\nThe Adjoint of a Matrix is:", '\n', Adjoint_of_A)