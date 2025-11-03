#Practical 1: Create and transform vectors and matrices (the transpose vector (matrix) conjugate
 #transpose of a vector (matrix))
#Program to transpose a matrix

import numpy as np

# Define the matrix directly
matrix = np.array([[1, 2], [3, 4], [5, 6]])

print("Matrix X is as follows:", '\n', matrix)

#For transposing the matrix
print("Transpose of matrix X is as follows:",'\n',np.transpose(matrix))