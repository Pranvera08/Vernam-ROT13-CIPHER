import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))