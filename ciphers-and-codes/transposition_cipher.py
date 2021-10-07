import math

def main():
    message = input("Write the message you want to cipher:\n")
    key = int(input("Write the number of keys: "))
    lines = math.ceil(len(message)/key) % key
    white_spaces = lines * key - len(message)
    message += " " * white_spaces
    cipher_or_decipher(message, key, lines)

def cipher(plaintext, key):
    ciphertext = [""]*key
    for letter in range(len(plaintext)):
        ciphertext[letter%key] += plaintext[letter]
    return ''.join(ciphertext)

def decipher(ciphertext, key, lines):
    plaintext = [""] * lines
    for letter in range(len(ciphertext)):
        plaintext[letter%lines] += ciphertext[letter]
    return ''.join(plaintext).strip()

def cipher_or_decipher(message, key, lines):
    print("1. Cipher")
    print("2. Decipher with key")
    print("3. Decipher by brute force")
    operation = input("2.  3. ")
    if operation == "1":
        output = cipher(message, key)
        print(" " + "_"*len(output))
        print("|" + output + "|")
        print(" " + "¯"*len(output))
    elif operation == "2":
        output = decipher(message, key, lines)
        print(" " + "_"*len(output))
        print("|" + output + "|")
        print(" " + "¯"*len(output))

if __name__ == "__main__":
    main()