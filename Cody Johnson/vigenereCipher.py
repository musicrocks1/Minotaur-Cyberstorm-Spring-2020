from sys import stdin, argv

def encrypt(plaintext, key):
    ciphertext = ""

    count = 0
    for letter in plaintext:
        offset = 0

        ##if the letter is uppercase, set the offset to uppercase
        if ord(letter) in range(65, 91):
            offset = 65
        ##if the letter is lowercase, set the offset to lowercase
        elif ord(letter) in range(97, 123):
            offset = 97

        ##if the offset was changed, then letter must be a valid uppercase/lowercase letter
        ##therefore, get the ASCII code of the key at the correct index indicated by count
        ##    and put it in the range of 0-25
        ##add the ASCII code of the letter, converted to 0-25
        ##mod by 26 and add the offset back, then convert to a letter and add it to the ciphertext
        ##increase the count by one
        if offset > 0:
            ciphertext += chr(((ord(key[count % len(key)]) - 97 + ord(letter) - offset) % 26) + offset)
            count += 1
        ##otherwise, just add the letter
        else:
            ciphertext += letter
    
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""

    count = 0
    for letter in ciphertext:
        offset = 0

        ##if the letter is uppercase, set the offset to uppercase
        if ord(letter) in range(65, 91):
            offset = 65
        ##if the letter is lowercase, set the offset to lowercase
        elif ord(letter) in range(97, 123):
            offset = 97

        ##if the offset was changed, then letter must be a valid uppercase/lowercase letter
        ##therefore, get the ASCII code of the letter, converted to 0-25
        ##subtract the ASCII code of the key at the correct index indicated by count
        ##    and put it in the range of 0-25
        ##mod by 26 and add the offset back, then convert to a letter and add it to the plaintext
        ##increase the count by one
        if offset > 0:
            plaintext += chr(((ord(letter) - offset - ord(key[count % len(key)]) + 97) % 26) + offset)
            count += 1
        ##otherwise, just add the letter
        else:
            plaintext += letter
            
    return plaintext

try:
    mode = argv[1]
    key = argv[2].replace(" ", "").lower()
except:
    print "Error. Please specify a mode and a key."
    exit()

text = stdin.read().rstrip("\n")

if (mode == "-e"):
    ciphertext = encrypt(text, key)
    print ciphertext
elif (mode == "-d"):
    plaintext = decrypt(text, key)
    print plaintext
