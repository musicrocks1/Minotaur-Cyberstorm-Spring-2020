############################################################################################
# Jacob Mathews
# Program 2 Vigenere Cipher
# 3/30/20
# Python Version 2.7
############################################################################################
from sys import stdin, argv
alphabet="abcdefghijklmnopqrstuvwxyz"   # valid letters for encryption

# takes a plaintext and key string then converts it to ciphertext using the Vigernere Cipher method
def encrypt(message, key):
    code = ""                           # encrypted message text
    letterVal = 0                       # index value of current encrypted character
    c = ""                              # letter value of the current encrypted character
    key = key.replace(" ","")           # remove spaces from key so message and key stay in sync

    # index values for current letter of message and key
    i=0                                 
    j=0                                 

    # iterates through each character of the message and converts to ciphertext
    while(i<len(message)):
        uppercase=0                     # tracks whether or not the current letter is uppercase
        m = message[i%len(message)]     # current letter of message
        k = key[j%len(key)]             # current letter of key
        
        # message and key are temporarily converted to lowercase 
        if(m.isupper()):               
            uppercase=1                 
        m = m.lower()
        k = k.lower()

        # if the current letter is not actually a letter, do not change it
        if(alphabet.find(m) == -1):
            c = m
            j-=1                        # j must be decremented to stay in sync
        else: 
            letterVal = (alphabet.find(m)+alphabet.find(k))%26  ## performs encryption method 
            c = alphabet[letterVal]                             ## to current letter

        # restores proper case
        if(uppercase):        
            c = c.upper()

        code += c                       # records current encrypted letter 

        # increment index values
        i+=1 
        j+=1
    
    return code

# takes a ciphertext and key string then converts it to plaintext using the Vigernere Cipher method
def decrypt(code, key):
    message = ""                        # decrypted text
    letterVal = 0                       # index value of the current decrypted character                 
    m = ""                              # letter value of the current decrypted character
    key = key.replace(" ","")           # removes spaces from key so

    # index values for the current letter of the ciphertext and key
    i=0
    j=0

    # iterates through each character of the ciphertext and converts to plaintext 
    while(i<len(code)):
        uppercase=0                     # tracks wheter or not the current letter is uppercase
        c = code[i%len(code)]           # current letter of ciphertext
        k = key[j%len(key)]             # current letter of the key

        # ciphertext and key are temporarily converted to lowercase
        if(c.isupper()):
            uppercase=1
        c = c.lower()
        k = k.lower()

        # if the current letter is not actually a letter, do not change it
        if(alphabet.find(c) == -1):
            m = c
            j-=1                        # j must be decremented to stay in sync
        else: 
            letterVal = (alphabet.find(c)-alphabet.find(k))%26  ## performs decyption method
            m = alphabet[letterVal]                             ## to current letter

        # restores proper case
        if(uppercase):
            m = m.upper()
            
        message += m                    # records current decrypted letter

        # increment index values
        i+=1
        j+=1
    
    return message

##############
#    MAIN    #
##############
# error handling for arguments inputted
if (len(argv)!= 3):
    print "INVALID INPUT"
    print "Follow the format of:"
    print "\n[program name] [mode] [key]"
    print "EX: P2-VigenereCipher.py -e \"my key\""
else:   
    mode = argv[1]                      # first parameter is mode
    key = argv[2]                       # second parameter is key
    text = stdin.read().rstrip("\n")
    
    # calls proper method based on inputted parameter
    if(mode=="-e"):
        print encrypt(text, key)
    elif(mode=="-d"):
        print decrypt(text,key)
        
    # error handling for incorrect mode
    else:
        print "INVALID INPUT"
        print "Valid modes are '-e' to encrypt a message or '-d' to decrypt a message"

