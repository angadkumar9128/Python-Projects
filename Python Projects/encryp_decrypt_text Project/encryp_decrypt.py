def encode_caesar_cipher(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decode_caesar_cipher(encrypted_text, shift):
    decoded_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decoded_char = chr((ord(char) - shift - 97) % 26 + 97)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text

# User input
user_input = input("Enter a text: ")

# Encoding
shift = 3
encoded_text = encode_caesar_cipher(user_input, shift)
print("Encoded Text:", encoded_text)

# Decoding
encoded_text=input("Decoded Text:")
decoded_text = decode_caesar_cipher(encoded_text, shift)
print("Decoded Text:", decoded_text)