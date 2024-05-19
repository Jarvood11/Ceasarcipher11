# Caesar Cipher
# Source code for caesarCipher

import pyperclip

# the string to be encrypted or decrypted
#message = 'This is my secret message.'

message = ' GUVF VF ZL FRPERG ZRFFNTR.'

# the encryption or decryted key
key = 13

# tells the program to encrypt or decrypt
#mode = 'encrypt'  # set to 'encrypt' or 'decrypt'
mode ='decrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ' '

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message strring
for symbol in message:
    if symbol in LETTERS:
        # get the encryption(or decryption) number for this symbol
        num = LETTERS.find(symbol)  # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encryption/decryption number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)

# copy the encrypted/decrypyed string to the screen
pyperclip.copy(translated)
