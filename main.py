# COLORS
GREEN="\033[92m"
RED="\033[91m"
CYAN="\033[96m"
YELLOW="\033[93m"
RESET="\033[0m"
def main():
    while True:
        print("/n"+ CYAN + "========== CRYPTO TOOL =========="+ RESET)
        print("1. Vernam Cipher")
        print("2. ROT13")
        print("0. EXIT")

        choice = input("Enter your choice: ")

        if choice == "0":
            print(CYAN + "Progam ended." + RESET)
            break

        else:
            print(RED + "Ivalid option!" + RESET)

if __name__ == "__main__":
    main()
