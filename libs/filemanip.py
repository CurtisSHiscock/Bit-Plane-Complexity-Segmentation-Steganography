#filemanip.py
import numpy as np
from graycode import *

## Methods for converting files to binary arrays and their inverse

# Methods to convert to binary
def messageToBinString(message): #May need a string builder, be careful
	'''
	Convert a string of characters to a binary string
	'''
	s = ""
	for i in range (len(message)):
		s+=char_to_binary(message[i])
	return s

def pad(bin_string): #Concatenation again
	'''
	Pad a binary string using #PKCS
	'''
	pad_required = (64 - len(bin_string) % 64) / 8 
	for i in range(pad_required):
		bin_string = '{0:08b}'.format(pad_required) + bin_string
	return bin_string

def char_to_binary(char):
	'''
	Convert char to binary
	'''
	x = ord(char)
	return '{0:08b}'.format(x)

def unpad(bin_string):
	'''
	Unpad a binary string using #PKCS
	'''
	pad_count = int(bin_string[0:8],2)
	#check padding
	for x in xrange(0, pad_count*8, 8):
		if(bin_string[x:x+8] != bin_string[0:8]):
			return bin_string
	return bin_string[pad_count*8: len(bin_string)]

def binStringtoSquares(bin_string):
	'''
	Convert binary string into a (8,8,X) matrix
	'''
	num_squares = len(bin_string)/64
	output_array = np.zeros((8,8,num_squares), dtype = 'uint8')
	counter = 0
	for i in range (8):
		for j in range (8):
			for k in range (num_squares):
				output_array[i,j,k] = bin_string[counter]
				counter+= 1
	return output_array

# Methods for converting from binary to characters

def bin_to_char(a):
	'''
	Convert binary string to character
	'''
	x=int(a,2)
	return chr(x)

def binStringtoFile(bin_string):
	'''
	Convert binary string to character string
	'''
	bin_string_holder = ""
	file = ""
	for i in range (len(bin_string)):
		bin_string_holder += bin_string[i]
		if((i+1)%8 == 0):
			file += bin_to_char(bin_string_holder)
			bin_string_holder = ""
	return str(file)

def convert_array_to_bin_string(array):
	'''
	Convert array to bin strings
	'''
	bin_string = ""
	for i in range (8):
		for j in range (8):
			for k in range (len(array[0,0])): 
				bin_string += str(array[i,j,k])
	return bin_string