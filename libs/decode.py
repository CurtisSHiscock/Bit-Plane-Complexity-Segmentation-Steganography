#decode.py
from filemanip import *
from embed import *
from PIL import Image
from compression import *

class Decoder(object):
	'''
	Wrapper class for all decoding operations
	'''
	def __init__(self, vessel, alpha):
		self.vessel = vessel
		self.alpha = alpha

	def bitPlaneArr(self):
		image = Image.open(self.vessel).convert('RGBA')
		array = np.array(image)
		self.bitPlaneArr = ImageSlice(array)

	def extract(self):
		reconstructed_binData = decode(self.bitPlaneArr, self.alpha)
		reconstructed_binString = unpad(convert_array_to_bin_string(reconstructed_binData))
		recontructed_secretFile = binStringtoFile(reconstructed_binString)
		decompress(recontructed_secretFile)