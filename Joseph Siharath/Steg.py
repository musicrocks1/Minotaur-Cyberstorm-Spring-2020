# Name: Joseph Siharath
# Due Date: 5/8/20
# Description: This program attempts to find a hidden message in a file by going through bytes or bits of the file

# NOTE: This program uses python2.7

from sys import stdin, stdout, argv, exit

# NOTE: If DEBUG is True and is outputing to a file, it WILL NOT RUN as it is adding the debug print outs
DEBUG = False

# Sentinel Bytes
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

# Constants and Variables
OPERATION = argv[1]
MODE = argv[2]
offset = argv[3]
interval = argv[4]
wrapperFile = argv[5]
 
# Checking for a hidden file if operation is storage
if (OPERATION == "-s"):
	hiddenFile = argv[6]
	hiddenFile = hiddenFile[2:]
	with open(hiddenfile, 'r') as f:
		hidden = bytearray(f.read())


# Stripping offset, interval, and wrapper into integers or byte arrays
offset = int(offset[2:])
interval = int(interval[2:])
wrapperFile = wrapperFile[2:]
with open(wrapperFile, 'r') as f:
	wrapper = bytearray(f.read())

# Storage
if (OPERATION == "-s"):
	if (DEBUG == True):
		print ("Storage")

	# Byte Method
	if (MODE == "-B"):
		if (DEBUG == True):
			print ("Byte Method")

		# Progresses through wrapper replacing the bytes in the wrapper at the
		# interval until it reaches the end of hidden message and then adds the
		# Sentinel Bytes
		i = 0
		while (i < len(hidden)):
			wrapper[offset] = hidden[i]
			offset += interval
			i += 1
		i = 0
		while (i < len(SENTINEL)):
			wrapper[offset] = SENTINEL[i]
			offset += interval
			i += 1
	# Bit Method
	if (MODE == "-b"):
		if (DEBUG == True):
			print ("Bit Method")

		i = 0
		while (i < length(hidden)):
			for j in range(0,8):
				wrapper[offset] = wrapper[offset] & 11111110
				wrapper[offset] = wrapper[offset] | ((hidden[i] & 10000000) >> 7)
				hidden[i] = (hidden[i] << 1) & (2 ** 8 - 1)
				offset += interval
			i += 1
		i = 0
		while (i < len(SENTINEL)):
			for j in range(0,8):
				wrapper[offset] = wrapper[offset] & 11111110
				wrapper[offset] = wrapper[offset] | ((SENTINEL[i] & 10000000) >> 7)
				SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
	
	# Output
	stdout.write(wrapper)

	# Invalid Mode Check
	if ((MODE != "-B") and (MODE != "-b")):
		print ("ERROR: Invalid Mode \nPlease input a valid mode: -B or -b")
	

# Extraction
if (OPERATION == "-r"):
	if (DEBUG == True):
		print ("Extraction")

	hidden = bytearray()
	# Byte Method
	if (MODE == "-B"):
		if (DEBUG == True):
			print ("Byte Method")

		# Progresses through the wrapper until it hits the Sentinel bytes or the end
		# of file
		while (offset < len(wrapper)):
			byte = wrapper[offset]
			# Checking if byte is the first Sentinel byte
			if (byte == SENTINEL[0]):
				i = 0 
				offsetTest = offset
				sentinelCheck = wrapper[offset]
				# Checks the next bytes in the pattern for Sentinel bytes
				# and if they match, break out of the while loop
				while (i < 5):
					i+=1
					offsetTest += interval
					sentinelCheck = wrapper[offsetTest]
					if (sentinelCheck != SENTINEL[i]):
						break
				if (i == 5):
					break

			hidden.append(byte)
			offset += interval

	# Bit Method
	if (MODE == "-b"):
		if (DEBUG == True):
			print ("Bit Method")
		
		
		i = 0
		while (offset < len(wrapper)):
			byte = 0
			# Forms the byte by going through each bit and masking all the bits
			# except for the LSb
			for j in range(0,8):
				byte = byte | (wrapper[offset] & 00000001)
				if (j < 7):
					byte = (byte << 1) & (2 ** 8 - 1)
					offset += interval
			# Checks for further Sentinel bytes by going through the process
			# until the bytes match all Sentinel bytes or fails to match
			if (byte == SENTINEL[0]):
				i = 0
				offsetTest = offset
				while (i<5):
					i +=1
					offsetTest += interval
					test = 0
					for j in range(0,8):
						test = test | (wrapper[offsetTest] & 00000001)
						if (j < 7):
							test = (test << 1) & (2 ** 8-1)
							offsetTest += interval
					if (test == SENTINEL[i]):
						pass
					else:
						break
				if (i == 5):
					break

	
			hidden.append(byte)
			offset += interval


	# Invalid Mode Check
	if ((MODE != "-B") and (MODE != "-b")):
		print ("ERROR: Invalid Mode \nPlease input a valid mode: -B or -b")
		exit(0)
	
	# Output
	stdout.write(hidden)
	

# Invalid Operation Check
if ((OPERATION != "-s") and (OPERATION != "-r")):
	print ("ERROR: Invalid Operation \nPlease input a valid operation: -r or -s")
	exit(0)




