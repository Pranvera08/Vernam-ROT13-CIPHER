def decrypt(cipher, key):
    result = ""
    key_index = 0

    cipher = cipher.upper()

    for c in cipher:
        if c.isalpha():
            pass
        else:
            result += c

    return result