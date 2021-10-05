"""Extended Caeser Cipher"""
import string

#extended list of symbols, instead of using the usual 25 letters
symbols = string.ascii_letters + string.digits + string.punctuation + " "
txtIn = input("Type the message you want to cipher or decipher:\n")
txtOut = ""

def get_key():
    get_key.key = input("Key: ")
    while get_key.key.isnumeric() == False:
        get_key.key = input("Input a valid number: ")
    get_key.key = int(get_key.key)

def encrypt(txtIn, txtOut):
    get_key()
    for letter in txtIn:
        oldIndex = symbols.find(letter)
        newIndex = oldIndex + get_key.key
        #check if the key is bigger than the symbols list
        if abs(newIndex) > len(symbols):
            newIndex = newIndex % len(symbols)
        txtOut = txtOut + symbols[newIndex]
    print(txtOut)

def decrypt(txtIn, txtOut):
    get_key()
    for letter in txtIn:
        oldIndex = symbols.find(letter)
        newIndex = oldIndex - get_key.key
        #check if the key is bigger than the symbols list
        if abs(newIndex) > len(symbols):
            newIndex = newIndex % len(symbols)
        txtOut = txtOut + symbols[newIndex]
    print(txtOut)

def brute_force(txtIn, txtOut):
    for key in range(len(symbols)):
        txtOut = ""
        for letter in txtIn:
            oldIndex = symbols.find(letter)
            newIndex = oldIndex - key
            txtOut = txtOut + symbols[newIndex]
        print(f"Key #{key}: {txtOut}")

def encryption_or_decryption():
    en_de = input("(e)ncryption or (d)ecryption: ")
    if en_de == "e":
        encrypt(txtIn, txtOut)
    elif en_de == "d":
        bf_or_key = input("Using the (k)ey or (b)rute force?: ")
        if bf_or_key == "k":
            decrypt(txtIn, txtOut)
        elif bf_or_key == "b":
            brute_force(txtIn, txtOut)
    else:
        print("Choose a valid option.")
        encryption_or_decryption()

encryption_or_decryption()