#encode.py
from filemanip import *
from embed import *
from complexity import *
from PIL import Image
from compression import *

class Encoder(object):
	'''
	Wrapper class for all encoding operations
	'''
	def __init__(self, infile, outfile, vessel, alpha):
		self.infile = infile
		self.outfile = outfile
		self.vessel = vessel
		self.alpha = alpha
		self.binData = self.binData()
		self.bitPlaneArr = self.bitPlaneArr()

	def binData(self):
		zipFile = compress(self.infile)
		binString = pad(messageToBinString(zipFile))
		return binStringtoSquares(binString)
		
	def bitPlaneArr(self):
		image = Image.open(self.vessel).convert('RGBA')
		uint8Arr = np.array(image)
		return ImageSlice(uint8Arr)

	def verify(self):
		if(not verifyCapacity(self.bitPlaneArr, self.binData, self.alpha)):
			print("Insufficient vessel capacity")
			exit()

	def embed(self):
		self.bitPlaneArr = encode(self.bitPlaneArr, self.binData, self.alpha)

	def reconstruct(self):
		stacked_embedded_bitPlaneArr = ImageStack(self.bitPlaneArr)
		reconstructed_vessel = Image.fromarray(stacked_embedded_bitPlaneArr)
		reconstructed_vessel.save(self.outfile, compress=1)