def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, a, b):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                ciphertext += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Kunci a tidak memiliki invers modular."

    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                plaintext += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
a = 5
b = 8
plaintext = "Fadhil khoiron naufal"
encrypted_text = encrypt(plaintext, a, b)
decrypted_text = decrypt(encrypted_text, a, b)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
