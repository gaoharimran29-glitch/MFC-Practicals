# Practical 10: Application of Linear algebra: Coding and decoding of 
# messages using nonsingular matrices.

import numpy as np

def encode(message, key_matrix):
    """Encodes a message string using a key matrix."""
    
    char_to_num = {char: i + 1 for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    char_to_num[' '] = 0

    message = message.upper()
    num_vector = [char_to_num.get(char, 0) for char in message]

    n = key_matrix.shape[0]
    remainder = len(num_vector) % n
    if remainder != 0:
        padding = n - remainder
        num_vector.extend([0] * padding) # Pad with spaces

    num_cols = len(num_vector) // n
    message_matrix = np.array(num_vector).reshape(num_cols, n).T

    encoded_matrix = key_matrix @ message_matrix
    return encoded_matrix

def decode(encoded_matrix, key_matrix):
    """Decodes a numeric matrix back into a message string."""
    
    try:
        inv_key_matrix = np.linalg.inv(key_matrix)
    except np.linalg.LinAlgError:
        return "Error: Key matrix is singular and cannot be inverted."

    decoded_matrix = np.round(inv_key_matrix @ encoded_matrix).astype(int)

    num_vector = decoded_matrix.T.flatten()

    num_to_char = {i + 1: char for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    num_to_char[0] = ' '
    
    message = "".join([num_to_char.get(num, '?') for num in num_vector])
    
    return message.strip() # Remove extra padding

# --- Define the Key and Message ---
K = np.array([
    [1, 2, 1],
    [2, 3, 2],
    [1, 1, 2]
])

message = "Linear Algebra is Fun"

print("--- Practical 10: Cryptography ---")
print(f"Original Message: {message}")
print(f"Key Matrix (K):\n{K}")

# --- Encode ---
encoded_data = encode(message, K)
print(f"\nEncoded Matrix (C = K * M):\n{encoded_data}")

# --- Decode ---
decoded_message = decode(encoded_data, K)
print(f"\nDecoded Message: {decoded_message}")