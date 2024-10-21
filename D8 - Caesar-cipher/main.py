import art
from time import sleep
from random import randint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
print()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def load(method):
    print(f"{method} in progress...")
    sleep(1)
    for i in range(10):
        print(" = ", end="")
        sleep(randint(1, 5) * 0.2)
    print(" > >")
    sleep(1)

def encrypt(text, shift):
    load("Encryption")
    plain_text = text.lower()
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            new_char = alphabet[new_index]
            cipher_text += new_char
        else:
            cipher_text += char
    return cipher_text

# Testing encyption
# print(encrypt(text, shift))

def decrypt(cipher_text, shift):
    load("Decryption")
    plain_text = ''
    for char in cipher_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % 26
            new_char = alphabet[new_index]
            plain_text += new_char
        else:
            plain_text += char
    return plain_text

# Testing decryption
# print(decrypt(text, shift))

if direction == 'encode':
    print(encrypt(text, shift))
elif direction == 'decode':
    print(decrypt(text, shift))
else:
    print("Invalid input. Please enter 'encode' or 'decode'.")
