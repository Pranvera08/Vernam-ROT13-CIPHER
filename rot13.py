def transform(text):
    """
    ROT13 transformation (same for encrypt/decrypt)
    """
    output = []
    for ch in text:
        if ch.isalpha():
            shift = 13
            start = ord('A') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - start + shift) % 26 + start)
            output.append(new_char)
        else:
            output.append(ch)

    return "".join(output)
def encrypt(text):
    return transform(text)