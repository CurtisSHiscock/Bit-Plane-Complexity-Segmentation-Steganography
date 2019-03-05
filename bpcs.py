#!/usr/bin/env python
'''
Author: Curtis Hiscock
A Bit-Plane Complexity Segmentation program based on an undergraduate research project at the University of Florida

Based on 'Principle of BPCS-Steganography by Eiji Kawguchi and Richard Eason'

More Info: http://datahide.org/BPCSe/principle-e.html
'''
import sys
sys.path.insert(0, './libs')

from encode import Encoder
from decode import Decoder
import argparse

parser = argparse.ArgumentParser(description='a Bit-Plane Complexity Segmentation application')
parser.add_argument('op', choices=['encode', '-e', 'decode', '-d'], help="desired operation operation")
parser.add_argument('-infile', '-e', help="path to embedding file(file to be embedded)(.png)")
parser.add_argument('-vessel', '-v', help="path to vessel file(file to embed data within)")
parser.add_argument('-alpha', '-a', default = 0.3, help="complexity threshold")
parser.add_argument('-outfile', '-o', default = "embedded_vessel.png", help="desired vessel output name(default 'embedded_vessel.png')")
args=parser.parse_args()

#args
op = args.op
alpha = args.alpha
infile = args.infile
vessel = args.vessel
outfile = args.outfile

if(op == 'encode' or op == '-e'): #encode
	encoder = Encoder(infile, outfile, vessel, alpha)
	print("Verifying image capacity...")
	encoder.verify()
	print("Embedding data into vessel...")
	encoder.embed()
	print("Reconstructing vessel...")
	encoder.reconstruct()
elif(op == 'decode' or op == '-d'): #decode
	decoder = Decoder(outfile, alpha)
	print("Retreiving data from vessel...")
	decoder.bitPlaneArr()
	print("Extracting files...")
	decoder.extract()
else:
	parser.print_help()