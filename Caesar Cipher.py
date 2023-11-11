def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Shift the character by the specified amount
            char_code = ord(char) + shift

            # Wrap around the alphabet if needed
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26

            # Append the encrypted character to the result
            encrypted_text += chr(char_code)
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    # Decryption is just encryption with a negative shift
    return caesar_cipher_encrypt(text, -shift)

# Example usage:
plaintext = "Fadhil Khoiron "
shift_amount = 3

encrypted_text = caesar_cipher_encrypt(plaintext, shift_amount)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_amount)
print(f"Decrypted text: {decrypted_text}")
