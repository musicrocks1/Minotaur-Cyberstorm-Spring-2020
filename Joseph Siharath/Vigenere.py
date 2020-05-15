# Name: Joseph Siharath
# Due Date: March 30, 2020
# Description: This program takes in plaintext from standard input and either decrypts or encrypts based off of user input and key given


from sys import stdin, argv, exit

# alphabet used to determine what letter to add to the output string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, newkey):
	# creates variables that makes all the letters in the key and plaintext uppercase to use the Vigenere algorithm
	uppertext = plaintext.upper()
	ciphertext = ""
	i = 0
	j = 0

	upperkey = newkey.upper()

	# For loop that goes through the text one character at a time and encrypts letters and just 
	# adds special characters to the output
	for i in range(len(plaintext)):

		
		if (not plaintext[i].isalpha()):
			ciphertext += plaintext[i]

		else:


			if (j >= len(newkey)):
				j = 0

			x = (ord(uppertext[i]) + ord(upperkey[j])) 
			x = x % 26
			k = alphabet[x]
			if (plaintext[i].islower()):
				k = k.lower()
			ciphertext += k
			j += 1

		
	return ciphertext

def decrypt (ciphertext, key):

	# Receives the ciphertext and key and capitalizes the letters into new variables
	plaintext = ""
	uppertext = ciphertext.upper()
	i = 0
	j = 0

	upperkey = newkey.upper()

	# For loop that goes through each character and decrypts every letter and adds 
	# special characters to the output
	for i in range(len(ciphertext)):

		if (not ciphertext[i].isalpha()):
			plaintext += ciphertext[i]

		else:
			if ( j >= len(newkey)):
				j = 0

			x = (26 + ord(uppertext[i]) - ord(upperkey[j]))
			x = x % 26
			k = alphabet[x]
			if (ciphertext[i].islower()):
				k = k.lower()
			plaintext += k
			j += 1


	return plaintext


text = stdin.read().rstrip("\n")


# Error Checking to see if user gave all inputs(user must hit Ctrl+D to actually exit)
if (len(argv) != 3):
	print "You must give a mode: -e to encrypt or -d to decrypt and you must give a key"
	exit(0)

mode = argv[1]
key = argv[2]
newkey = ""
z =0
for z in range(len(key)):
	if (not " " in key[z]):
		newkey += key[z]

if (mode == "-e"):
	ciphertext = encrypt(text, newkey)
	print ciphertext

elif (mode == "-d"):
	plaintext = decrypt(text, newkey)
	print plaintext
