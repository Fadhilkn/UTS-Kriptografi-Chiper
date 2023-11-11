def polyalphabetic_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    plaintext = plaintext.upper()

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            # Menghitung shift sesuai dengan kunci
            shift = ord(key[i % key_length]) - ord('A')

            if char.islower():
                ciphertext += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            ciphertext += char

    return ciphertext

def polyalphabetic_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    ciphertext = ciphertext.upper()

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Menghitung shift sesuai dengan kunci
            shift = ord(key[i % key_length]) - ord('A')

            if char.islower():
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            plaintext += char

    return plaintext

# Contoh penggunaan
key = "KEY"
plaintext = "Fadhil"
ciphertext = polyalphabetic_encrypt(plaintext, key)
decrypted_text = polyalphabetic_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text)
