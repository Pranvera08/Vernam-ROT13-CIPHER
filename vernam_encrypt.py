import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(plaintext, key):
    result = ""
    key_index = 0

    plaintext = plaintext.upper()