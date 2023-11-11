import numpy as np

def text_to_matrix(text, n):
    # Convert the text to a matrix of numbers (ASCII values)
    matrix = [ord(char) - ord('A') for char in text]

    # Pad the matrix with zeros if needed
    while len(matrix) % n != 0:
        matrix.append(0)

    # Reshape the matrix to a 2D matrix with n columns
    return np.array(matrix).reshape(-1, n)

def matrix_to_text(matrix):
    # Convert a matrix of numbers back to text
    return ''.join([chr(num % 26 + ord('A')) for num in matrix.flatten()])

def matrix_modulo_inverse(matrix, mod):
    # Calculate the modular inverse of a matrix
    det = int(np.linalg.det(matrix))
    det_inv = pow(det, 1, mod) if det % mod != 0 else 0

    adjugate = np.round(det_inv * np.linalg.inv(matrix) * det) % mod

    return adjugate.astype(int)

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext_matrix = text_to_matrix(plaintext, n)

    # Encrypt the matrix using matrix multiplication
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26

    # Convert the encrypted matrix back to text
    encrypted_text = matrix_to_text(encrypted_matrix)

    return encrypted_text

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key_matrix_inv = matrix_modulo_inverse(key_matrix, 26)

    ciphertext_matrix = text_to_matrix(ciphertext, n)

    # Decrypt the matrix using matrix multiplication with the inverse key matrix
    decrypted_matrix = np.dot(ciphertext_matrix, key_matrix_inv) % 26

    # Convert the decrypted matrix back to text
    decrypted_text = matrix_to_text(decrypted_matrix)

    return decrypted_text

# Contoh penggunaan:
plaintext = "fadhil"
key_matrix = np.array([[6, 24], [1, 13]])

encrypted_text = hill_cipher_encrypt(plaintext, key_matrix)
print(f"Teks Terenkripsi: {encrypted_text}")

decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
print(f"Teks Terdekripsi: {decrypted_text}")
