#compression.py
import zlib, base64
import zipfile
import os

## Compression methods

def compress(filename):
	'''
	Given a filename arg, returns a compressed file object with the file's contents
	'''
	zipfile.ZipFile('o.zip', 'w', zipfile.ZIP_DEFLATED).write(filename, os.path.basename(filename))

	with open('o.zip', 'rb') as file:
		val = file.read()

	os.remove('o.zip')
	return val

def decompress(filename):
	'''
	Decompresses and extracts zipfile contents
	'''
	with open('o.zip', 'wb') as x:
		x.write(filename)

	with zipfile.ZipFile('o.zip', 'r') as myZip:
		print("Recovered " + str(len(myZip.namelist())) + " Files: ")
		for i in range (len(myZip.namelist())):
			print(myZip.namelist()[i])
		myZip.extractall()

	os.remove('o.zip')