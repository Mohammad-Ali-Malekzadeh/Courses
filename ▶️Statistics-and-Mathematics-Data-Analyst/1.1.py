import numpy as np

# Define two Vectors
U = np.array([3, 4, 5])
V = np.array([1, 2, 3])

# Perform Arithmetic Operations
vector_sum = U + V # Addition
vector_difference = U - V # Subtraction
vector_product = U * V # Element-wise Multiplication
scalar_multiplication = 2 * U # Scalar Multiplication
dot_product = np.dot(U, V) # Dot Product
vector_norm = np.linalg.norm(U) # Magnitude of Vector U

print("Vector Sum:", vector_sum)
print("Vector Difference:", vector_difference)
print("Element-wise Multiplication:", vector_product)
print("Scalar Multiplication:", scalar_multiplication)
print("Dot Product:", dot_product)
print("Magnitude of Vector U:", vector_norm)