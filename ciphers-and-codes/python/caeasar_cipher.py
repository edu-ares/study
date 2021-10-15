"""Caesar Cipher"""

def main():
    """Get the message, list of symbols and type of operation from the user"""
    symbols = get_symbol_list()
    message = get_plaintext(symbols)
    output = operation(message, symbols)
    print(output)

def operation(message, symbols):
    """Get user input for the type of operation"""
    print("\nWhat kind of operation do you want to perform on the message?" +
          "\nType: \n(1) to cipher the message (default)" +
          "\n(2) to decipher it \n(3) to brute force")
    mode = input()
    if mode == "3":
        brute_force(message, symbols)
        output = ""
    elif mode == "2":
        key = get_key(symbols)
        output = decipher(message, symbols, key)
    else:
        key = get_key(symbols)
        output = cipher(message, symbols, key)
    return output

def get_symbol_list():
    """Generate the list of symbols for the cipher"""
    sym_dict = {"upper": list(range(65, 90)),
                    "lower": list(range(97, 122)),
                    "nums": list(range(48, 58)),
                    "all": list(range(32, 126)),
                    "others": list(range(32, 48)) + list(range(58, 65)) +
                    list(range(91, 97)) + list(range(123, 127)),
                    }
    symbols = input("Select a list of symbols: \n1. Lowercase only" +
    "\n2. Uppercase only" + "\n3. Letters(lowercase and uppercase)" +
    "\n4. Letters and numbers" + "\n5. (default) Letters, numbers and symbols.\n")
    symbol_list = ""
    if symbols == "1":
        for letter in sym_dict["lower"]:
            symbol_list += chr(letter)
    elif symbols == "2":
        for letter in sym_dict["upper"]:
            symbol_list += chr(letter)
    elif symbols == "3":
        for letter in sym_dict["lower"] + sym_dict["upper"]:
            symbol_list += chr(letter)
    elif symbols == "4":
        for letter in sym_dict["lower"] + sym_dict["upper"] + sym_dict["nums"]:
            symbol_list += chr(letter)
    else:
        for letter in sym_dict["all"]:
            symbol_list += chr(letter)
    return symbol_list

def get_plaintext(symbols):
    """Get the message and check if the chracters are present in symbols"""
    message = input("\nType the message you want to cipher or decipher?\n")
    while not set(message) <= set(symbols):
        message = input(
            "\nThe symbol(s) in the message doesn't exist" +
            " in our current list of symbols.\n" +
            "Write a new message to use:\n")
    while message == "":
        message = input("\nYour message is empty.\n" +
                        "Write a message to continue:\n")
    return message

def get_key(symbols):
    """Get key to cipher or decipher the message"""
    key = input("\nWhat key do you want to use?\n")
    while key.isdigit() is False or key == "":
        # or int(key) >= len(symbols):
        print("\nThe key can't be empty or not be a number!")
        key = input("")
    return int(key)

def cipher(plaintext, symbols, key):
    """Cipher message with the provided key"""
    ciphertext = ""
    for letter in plaintext:
        index = symbols.find(letter)
        new_index = index + key
        #checks if new index is too big
        if new_index >= len(symbols):
            new_index %= len(symbols)
        ciphertext += symbols[new_index]
    return ciphertext

def decipher(plaintext, symbols, key):
    """Decipher message with the provided key"""
    ciphertext = ""
    for letter in plaintext:
        index = symbols.find(letter)
        #check if the key is big
        if key >= len(symbols):
            key %= len(symbols)
        new_index = index - key
        ciphertext += symbols[new_index]
    return ciphertext

def brute_force(plaintext, symbols):
    """Brute force all possible keys to decipher the message"""
    ciphertext = ""
    for key in range(len(symbols)):
        ciphertext = ""
        for letter in plaintext:
            old_index = symbols.find(letter)
            new_index = old_index - key
            ciphertext += symbols[new_index]
        print(f"Key #{key}: {ciphertext}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye, bye!")
