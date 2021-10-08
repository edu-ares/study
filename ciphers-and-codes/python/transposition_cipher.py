import math

def main():
    message = get_message()
    cipher_or_decipher(message)

def get_message():
    message = input("Write the message you want to cipher or decipher:\n")
    return message

def get_columns():
    """Get columns to cipher or decipher the message"""
    columns = input("Write the number of columns to divide the message: ")
    #checks if it is a valid input
    while columns.isnumeric() is False:
        columns = input("Input a valid number: ")
    columns = int(columns)
    return columns

def get_lines(message, columns):
    lines = math.ceil(len(message)/columns) % columns
    if lines == 0:
        lines = 1
    return lines

def get_white_space(message, columns, lines):
    #add white space at the end of the last line
    white_spaces = lines * columns - len(message)
    message += " " * white_spaces
    return message

def brute_force(ciphertext):
    for letter in range(1, len(ciphertext) + 1):
        columns = letter
        lines = get_lines(ciphertext, columns)
        get_white_space(ciphertext, columns, lines)
        plaintext = decipher(ciphertext, columns, lines)
        print("key #" + str(letter) + ". " + plaintext)

def cipher(plaintext, columns):
    """Cipher message"""
    ciphertext = [""]*columns
    for letter in range(len(plaintext)):
        ciphertext[letter%columns] += plaintext[letter]
    return ''.join(ciphertext)

def decipher(ciphertext, columns, lines):
    plaintext = [""] * lines
    for letter in range(len(ciphertext)):
        plaintext[letter%lines] += ciphertext[letter]
    return ''.join(plaintext).strip()

def cipher_or_decipher(message):
    print("1. Cipher")
    print("2. Decipher with columns")
    print("3. Decipher by brute force")
    operation = input()
    while operation.isnumeric() is False or int(operation) >= 4:
        operation = input("Input a valid number: ")
    if operation == "1":
        columns = get_columns()
        lines = get_lines(message, columns)
        message = get_white_space(message, columns, lines)
        output = cipher(message, columns)
        print(" " + "_"*len(output))
        print("|" + output + "|")
        print(" " + "¯"*len(output))
    elif operation == "2":
        columns = get_columns()
        lines = get_lines(message, columns)
        output = decipher(message, columns, lines)
        print(" " + "_"*len(output))
        print("|" + output + "|")
        print(" " + "¯"*len(output))
    elif operation == "3":
        brute_force(message)

if __name__ == "__main__":
    main()