# Function to encrypt the plain text
def caesar_encrypt(text, shift):
    encrypted_text = ""  # Empty string to store encrypted result
    for char in text:  # Loop through each character in the text
        # Check if character is uppercase letter
        if char.isupper():
            # Convert character to ASCII, shift it, wrap around using modulo 26
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_text += encrypted_char
        # Check if character is lowercase letter
        elif char.islower():
            # Convert character to ASCII, shift it, wrap around using modulo 26
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            # If character is space or special character, keep it unchanged
            encrypted_text += char
    return encrypted_text
# Function to decrypt the cipher text
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""  # Empty string to store decrypted result
    for char in ciphertext:
        # Check if character is uppercase letter
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_text += decrypted_char
        # Check if character is lowercase letter
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            # Keep spaces and special characters unchanged
            decrypted_text += char
    return decrypted_text
# Taking input from user
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
# Encrypt the message
encrypted_message = caesar_encrypt(message, shift_value)
print("Encrypted Message:", encrypted_message)
# Decrypt the message
decrypted_message = caesar_decrypt(encrypted_message, shift_value)
print("Decrypted Message:", decrypted_message)
