# Practical 13: Compute Curl of a vector field.

from sympy import symbols, diff, Matrix

# Define the variables
x, y, z = symbols('x y z')

# Define the components (P, Q, R) of the vector field F
P = x**2 * y
Q = -y**2 * z**2
R = 3 * x * y * z

# Store as a Matrix for easy display
F = Matrix([P, Q, R])

print("--- Practical 13: Curl of a Vector Field ---")
print(f"Vector Field F(x, y, z) =\n{F}")

# Calculate the partial derivatives needed for the curl
dR_dy = diff(R, y)
dQ_dz = diff(Q, z)

dP_dz = diff(P, z)
dR_dx = diff(R, x)

dQ_dx = diff(Q, x)
dP_dy = diff(P, y)

# Calculate the components of the curl vector
curl_i = dR_dy - dQ_dz
curl_j = dP_dz - dR_dx
curl_k = dQ_dx - dP_dy

# The curl is the vector of these components
curl_vector = Matrix([curl_i, curl_j, curl_k])

print("\nCurl of F (∇ × F):")
print(curl_vector)

print(f"\ni component: (dR/dy - dQ/dz) = {curl_i}")
print(f"j component: (dP/dz - dR/dx) = {curl_j}")
print(f"k component: (dQ/dx - dP/dy) = {curl_k}")