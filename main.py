import time

from vernam_encrypt import encrypt as v_encrypt, generate_key
from vernam_decrypt import decrypt as v_decrypt
from rot13 import encrypt as r_encrypt, decrypt as r_decrypt

# COLORS
GREEN="\033[92m"
RED="\033[91m"
CYAN="\033[96m"
YELLOW="\033[93m"
RESET="\033[0m"

def type_text(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def loading(message="Processing", dots=3, delay=0.4):
    print(YELLOW + message + RESET, end="", flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

def line():
    print("=" * 28)

def main():
    type_text(CYAN + "Welcome to the Crypto Tool." + RESET, 0.04)

    while True:
        print("/n"+ CYAN + "========== CRYPTO TOOL =========="+ RESET)
        print("1. Vernam Cipher")
        print("2. ROT13")
        print("0. EXIT")

        choice = input("Enter your choice: ")

        # VERNAM
        if choice == "1":
            print("/n1. Encrypt")
            print("2. Decrypt")
            option = input("Select: ")

            if option == "1":
                text = input("Enter plaintext: ")

                letters_only = sum(1 for ch in text if ch.isalpha())
                key = generate_key(letters_only)

                loading("Encrypting")
                cipher = v_encrypt(text, key)

                print("/n" + GREEN + "Ciphertext:" + RESET, cipher)
                print(CYAN + "Key:" + RESET, key)

            elif option == "2":
                cipher = input("Enter ciphertext: ")
                key = input("Enter key: ")

                try:
                    loading("Decrypting")
                    plain = v_decrypt(cipher, key)
                    print(GREEN + "Decrypted:" + RESET, plain)
                except Exception as e:
                    print(RED + "Error:" + RESET,e)

            else:
                print(RED + "Invalid option!" + RESET)

        # ROT13
        elif choice == "2":
            print("/n1. Encrypt")
            print("2. Decrypt")
            option = input("Select: ")

            text = input("Enter plaintext: ")

            if option == "1":
                loading("Encrypting")
                print(GREEN + "Encrypted:" + RESET, r_encrypt(text))
            elif option == "2":
                loading("Decrypting")
                print(GREEN + "Decrypted:" + RESET, r_decrypt(text))
            else:
                print(RED + "Invalid option!" + RESET)

        # EXIT
        elif choice == "0":
            loading("Closing program", 3, 0.3)
            print(CYAN + "Progam ended." + RESET)
            break

        else:
            print(RED + "Ivalid option!" + RESET)

if __name__ == "__main__":
    main()
