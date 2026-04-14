def decrypt(cipher, key):
    result = ""
    key_index = 0

    cipher = cipher.upper()

    for c in cipher:
        if c.isalpha():
            if key_index >= len(key):
                raise ValueError("Key length is not enough.")

            k = key[key_index].upper()

            c_num = ord(c) - ord('A')
            k_num = ord(k) - ord('A')

            p_num = (c_num - k_num) % 26
            result += chr(p_num + ord('A'))

            key_index += 1
        else:
            result += c

    return result