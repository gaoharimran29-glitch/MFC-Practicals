# Practical 11: Compute Gradient of a scalar field.

from sympy import symbols, diff, sin, cos, exp, Matrix

# Define the variables
x, y, z = symbols('x y z')

# Define the scalar field (function) f
f = x**2 * y**3 + exp(z) * cos(x)

print("--- Practical 11: Gradient of a Scalar Field ---")
print(f"Scalar Field f(x, y, z) = {f}")

# Calculate the partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)
df_dz = diff(f, z)

# The gradient is the vector of these partials
gradient_vector = Matrix([df_dx, df_dy, df_dz])

print("\nGradient of f (∇f):")
print(gradient_vector)

print(f"\nPartial derivative w.r.t x: {df_dx}")
print(f"Partial derivative w.r.t y: {df_dy}")
print(f"Partial derivative w.r.t z: {df_dz}")