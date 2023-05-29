# Aashra_Dangol_np03cs4a220218
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")
welcome()
def enter_message():
    mode = input("Would you like to encrypt(e) or decrypt(d): ").lower()
    while mode != "encrypt" and mode != "decrypt":
         mode = input("Invalid mode. Please enter 'e' to encrypt or 'd' to decrypt': ").lower()
    message = input("Enter the message: ")
    while True:
        try:
            shiftnum= int(input("Enter the shift number(1-26):"))
            if shiftnum>=1 and shiftnum<=26:
                return mode,message,shiftnum
            else:
                print("Invalid shift number. Number should be between 1-26")
        except ValueError:
            print("Invalid input, Please enter valid integer number only.")
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shiftn = ord(char) + key
            if char.isupper():
                if shiftn > ord('Z'):
                    shiftn -= 26
                final_char = chr(shiftn)
            else:
                if shiftn > ord('z'):
                    shiftn -= 26
                final_char = chr(shiftn)
            ciphertext += final_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shiftn = ord(char) - key
            if char.isupper():
                if shiftn < ord('A'):
                    shiftn += 26
                final_char = chr(shiftn)
            else:
                if shiftn < ord('a'):
                    shiftn += 26
                final_char = chr(shiftn)
            plaintext += final_char
        else:
            plaintext += char
    return plaintext

def main():
    while True:
        mode,message,shiftnum=enter_message() 
        if mode == "encrypt":
            ciphertext = encrypt(message, shiftnum)
            print("Ciphertext: ", ciphertext)
        else:
            plaintext = decrypt(message, shiftnum)
            print("Plaintext: ", plaintext)

        again = input("Would you like to encrypt/decrypt another message? (y/n) ").lower()
        while again != "y" and again != "n":
            again = input("Invalid input. Please enter either 'y' or 'n': ").lower()
        if again == "n":
            print("Thank you")
            break

if __name__ == "__main__":
    main()
