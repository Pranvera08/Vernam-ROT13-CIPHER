import time



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

def main():
    type_text(CYAN + "Welcome to the Crypto Tool." + RESET, 0.04)

    while True:
        print("/n"+ CYAN + "========== CRYPTO TOOL =========="+ RESET)
        print("1. Vernam Cipher")
        print("2. ROT13")
        print("0. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("/n1. Encrypt")
            print("2. Decrypt")
            option = input("Select: ")

            if option == "1":
                print(YELLOW + "Vernam encryption will be added soon." + RESET)

            elif option == "2":
                print(YELLOW + "Vernam decryption will be added soon." + RESET)

            else:
                print(RED + "Invalid option!" + RESET)


        elif choice == "0":
            loading("Closing program", 3, 0.3)
            print(CYAN + "Progam ended." + RESET)
            break

        else:
            print(RED + "Ivalid option!" + RESET)

if __name__ == "__main__":
    main()
