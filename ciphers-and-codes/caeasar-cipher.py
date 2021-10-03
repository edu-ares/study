symbols = " abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0123456789.?!@"

txtIn = input("Type the message you want to encrypt:\n")
key = int(input("Key: "))
en_de = input("(e)ncryption or (d)ecryption\n")
txtOut = ""

def encrypt(txtIn, key, txtOut):
    for letter in txtIn:
        oldIndex = symbols.find(letter)
        newIndex = oldIndex + key
        txtOut = txtOut + symbols[newIndex]
    print(txtOut)

def decrypt(txtIn, key, txtOut):
    for letter in txtIn:
        oldIndex = symbols.find(letter)
        newIndex = oldIndex - key
        txtOut = txtOut + symbols[newIndex]
    print(txtOut)

if en_de == "e":
    encrypt(txtIn, key, txtOut)
elif en_de == "d":
    decrypt(txtIn, key, txtOut)