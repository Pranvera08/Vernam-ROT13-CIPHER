import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(plaintext, key):
    result = ""
    key_index = 0

    plaintext = plaintext.upper()

        for p in plaintext:
        if p.isalpha():
            if key_index >= len(key):
                raise ValueError("Key length is not enough.")