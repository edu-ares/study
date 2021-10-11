import random
import sys
import string
import caeasar_cipher


def main():
    for i in range (1, 20):
        random.seed(i)
        number_of_tests = 100
        symbols = caeasar_cipher.get_symbol_list()
        message_list = get_message(number_of_tests, symbols)
        key = random.randint(0, len(symbols))
        for test in range(number_of_tests):
            print("Test " + str(test+1) + ": " + message_list[test][:50])
            encrypted_message = caeasar_cipher.cipher(
                message_list[test], symbols, key)
            decrypted_message = caeasar_cipher.decipher(
                encrypted_message, symbols, key)
            if decrypted_message == message_list[test]:
                print("It worked!")
            else:
                print("Original:\n" + message_list[test], "\nDecrypted:\n" + decrypted_message)
                # print("Failed.", file=sys.stderr)
                # print(message_list[test] + "\n")
                # print(decrypted_message)
                sys.exit()


def get_message(number_of_tests, symbols):
    message_list = [""] * (number_of_tests)
    for test in range(number_of_tests):
        # create a number of messages and print them
        message = symbols * random.randint(1, 25)
        message = list(message)
        random.shuffle(message)
        message = "".join(message)
        message_list[test] = message
    return message_list


if __name__ == "__main__":
    main()
