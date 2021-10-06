
"""Caesar Cipher"""
import string

def main():
    global message
    global symbols
    message = get_input()
    symbols = get_symbol_list(message)
    cipher_or_decipher()

def get_input():
    """Get the plaintext from the user"""
    txt_in = input("\nType the message you want to cipher or decipher:\n")
    return txt_in

def get_key():
    """Get key to cipher or decipherthe message"""
    key = input("\nKey: ")
    #checks if it is a valid input
    while key.isnumeric() is False:
        key = input("Input a valid number: ")
    key = int(key)
    #loop back to the symbol list if key + letter is too big
    while len(symbols) + key >= len(symbols):
        key = key - len(symbols)
    return key

def cipher(plaintext):
    """Cipher message with the provided key"""
    ciphertext = ""
    key = get_key()
    for letter in plaintext:
        old_index = symbols.find(letter)
        new_index = old_index + key
        ciphertext = ciphertext + symbols[new_index]
    return ciphertext

def decipher(plaintext):
    """Decipher the message with the provided key"""
    ciphertext = ""
    key = get_key()
    for letter in plaintext:
        old_index = symbols.find(letter)
        new_index = old_index - key
        ciphertext = ciphertext + symbols[new_index]
    return ciphertext

def brute_force(plaintext):
    """Brute force all possible keys to decipher the message"""
    ciphertext = ""
    for key in range(len(symbols)):
        ciphertext = ""
        for letter in plaintext:
            old_index = symbols.find(letter)
            new_index = old_index - key
            ciphertext = ciphertext + symbols[new_index]
        print(f"Key #{key}: {ciphertext}")

def get_symbol_list(plaintext):
    """list of symbols that will be used to cipher the text"""
    upca = string.ascii_lowercase
    lowca = string.ascii_uppercase
    numbers = string.digits
    punct = string.punctuation
    space = " "
    symbol_in = ""
    symbols_list = [upca + lowca + numbers + punct,
        upca + lowca + numbers, upca + lowca, upca, lowca]
    print("\nWhat list of symbols should be used?\n")
    for i in range(len(symbols_list)):
        print(f"{i+1}. {symbols_list[i]}")
    print("6. Make your own symbol list")
    select_symbol = input()
    if int(select_symbol) == 5:
        "Write the symbols you want in your list"
        symbol_in = input()
    elif int(select_symbol) < 5:
        symbol_in = symbols_list[int(select_symbol)-1] + space
    else:
        print("Input a valid option.")
    #check if the symbols in the mensage are inside the symbol list
    if not set(plaintext) <= set(symbol_in):
        print("\nSymbol list doesn't contain the same characters the message has.")
        input("Symbol list 1 selected.")
        symbol_in = symbols_list[0] + space
    return symbol_in

def cipher_or_decipher():
    """get user input for the type of operation"""
    ci_de = input("\n1.Cipher\n2.Decipher: \n")
    if ci_de == "1":
        print(cipher(message))
    elif ci_de == "2":
        bf_or_key = input("\n1.Using a key\n2.Brute force: \n")
        if bf_or_key == "1":
            print(decipher(message))
        else:
            brute_force(message)
        
    else:
        print("Choose a valid option.")
        cipher_or_decipher()

if __name__ == "__main__":
    main()
    