import random, sys, string, column_transposition_cipher

def main():
    random.seed(1)

    for i in range(100):
        message = string.ascii_letters * random.randint(1,25)
        message = list(message)
        random.shuffle(message)
        message = "".join(message)
        print(f"Test {i + 1}: {message[:50]}")

        key = random.randint(1, 10)
        encrypted_message = column_transposition_cipher.cipher(message, key)
        lines = column_transposition_cipher.get_lines(message, key)
        decrypted_message = column_transposition_cipher.decipher(encrypted_message, key, lines)
        if decrypted_message == message:
            print("It worked.")
        else:
            print(key)
            print("Failed.", file=sys.stderr)
            print(message + "\n")
            print("encripted message:\n" + encrypted_message + "\n")
            print("decripted message:\n" + decrypted_message + "\n")
            sys.exit()

if __name__ == "__main__":
    main()