# Practical 12: Compute Divergence of a vector field.

from sympy import symbols, diff, sin, exp, Matrix

# Define the variables
x, y, z = symbols('x y z')

# Define the components (P, Q, R) of the vector field F
P = x**2 * y
Q = -y**2 * z**2
R = 3 * x * y * z

# Store as a Matrix for easy display
F = Matrix([P, Q, R])

print("--- Practical 12: Divergence of a Vector Field ---")
print(f"Vector Field F(x, y, z) =\n{F}")

# Calculate the partial derivatives
dP_dx = diff(P, x)
dQ_dy = diff(Q, y)
dR_dz = diff(R, z)

# The divergence is the sum of these partials
divergence = dP_dx + dQ_dy + dR_dz

print(f"\nPartial P / Partial x = {dP_dx}")
print(f"Partial Q / Partial y = {dQ_dy}")
print(f"Partial R / Partial z = {dR_dz}")

print(f"\nDivergence of F (∇ · F) = {divergence}")