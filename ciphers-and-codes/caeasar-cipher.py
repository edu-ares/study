
"""Extended Caesar Cipher"""
import string

def main():
    global symbols
    global txt_in
    #extended list of symbols that will be used to cipher the text
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    #get the plaintext from the user
    txt_in = input("Type the message you want to cipher or decipher:\n")
    #ciphertext output
    cipher_or_decipher()

def get_key():
    #get key from user input
    key = input("Key: ")
    #checks if it is a valid input
    while key.isnumeric() is False:
        key = input("Input a valid number: ")
    key = int(key)
    #loop back to the symbol list if key + letter is too big
    if len(symbols) + key > len(symbols):
        key = key % len(symbols)
    return key

def cipher(plaintext):
    ciphertext = ""
    key = get_key()
    for letter in plaintext:
        old_index = symbols.find(letter)
        new_index = old_index + key
        ciphertext = ciphertext + symbols[new_index]
    return ciphertext

def decipher(plaintext):
    ciphertext = ""
    key = get_key()
    for letter in plaintext:
        old_index = symbols.find(letter)
        new_index = old_index - key
        ciphertext = ciphertext + symbols[new_index]
    return ciphertext

def brute_force(plaintext):
    ciphertext = ""
    for key in range(len(symbols)):
        ciphertext = ""
        for letter in plaintext:
            old_index = symbols.find(letter)
            new_index = old_index - key
            ciphertext = ciphertext + symbols[new_index]
        print(f"Key #{key}: {ciphertext}")

def cipher_or_decipher():
    ci_de = input("(c)ipher or (d)ecipher: ")
    if ci_de == "c":
        print(cipher(txt_in))
    elif ci_de == "d":
        bf_or_key = input("Using the (k)ey or (b)rute force?: ")
        if bf_or_key == "k":
            print(decipher(txt_in))
        elif bf_or_key == "b":
            brute_force(txt_in)
    else:
        print("Choose a valid option.")
        cipher_or_decipher()

if __name__ == "__main__":
    main()
    