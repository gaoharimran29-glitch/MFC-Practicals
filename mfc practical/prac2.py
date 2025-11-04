# Practical 2: Generate the matrix into echelon form and find its rank.
import numpy as np

matrix = np.array([[1, 3, 7, 2],
                   [2, 6, 14, 4],
                   [3, 1, 5, 0]])

print("Matrix X is as follows:", '\n', matrix)

# For finding the Rank of a Matrix
rank = np.linalg.matrix_rank(matrix)

print("The Rank of a Matrix is:", rank)