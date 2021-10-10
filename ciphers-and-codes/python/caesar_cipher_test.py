import random
import sys
import string
import caeasar_cipher


def main():
    random.seed(1)
    number_of_tests = 100
    message_list = get_message(number_of_tests)
    symbols = caeasar_cipher.get_symbol_list()
    key = random.randint(0, 93)
    for test in range(number_of_tests):
        print(message_list[test])
        encrypted_message = caeasar_cipher.cipher(
            message_list[test], symbols, key)
        decrypted_message = caeasar_cipher.decipher(
            encrypted_message, symbols, key)
        if decrypted_message == message_list[test]:
            print("It worked.")
        else:
            print("Failed.", file=sys.stderr)
            print(message_list[test] + "\n")
            print(decrypted_message)
            sys.exit()


def get_message(number_of_tests):
    message_list = [""] * (number_of_tests)
    for test in range(number_of_tests):
        # create a number of messages and print them
        message = string.ascii_letters * random.randint(1, 25)
        message = list(message)
        random.shuffle(message)
        message = "".join(message)
        message = "Test " + str(test+1) + ": " + message[:50]
        message_list[test] = message
    return message_list


if __name__ == "__main__":
    main()
