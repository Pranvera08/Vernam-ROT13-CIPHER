def main():
    while True:
        print("/n ========== CRYPTO TOOL ==========")
        print("1. Vernam Cipher")
        print("2. ROT13")
        print("0. EXIT")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Progam ended.")
            break

        else:
            print("Ivalid option!")

if __name__ == "__main__":
    main()
