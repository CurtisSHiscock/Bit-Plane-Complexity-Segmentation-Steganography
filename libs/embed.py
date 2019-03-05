#embed.py
import numpy as np
from complexity import *
from graycode import *

##Methods for encoding and decoding data into images

def ImageSlice(array): #TODO combine imageslice methods
    '''
    Driver for ImageSliceBackend

    NOTE: currently hard coded to work only on 'RGBA' (4 plane) arrays 
    '''
    bitPlaneArr  = np.zeros( (array.shape[0], array.shape[1], 32), dtype = 'uint8' )
    for i in range (4):
    	bitPlaneArr[:,:,slice(i*8,(i*8)+8)] = ImageSliceBackend(array[:,:,i])
    return bitPlaneArr

def ImageSliceBackend(array):
    '''
    Expands binary arrays of images into 8 bit planes. 
    '''
    shape = array.shape
    bitPlaneArr  = np.zeros( (shape[0], shape[1], 8), dtype = 'uint8' )
    for i in range(shape[0]):
        for j in range(shape[1]):
            bitArr = pbc_to_cgc(np.unpackbits(np.uint8(array[i,j])))
            for k in range(8):
                bitPlaneArr[i,j,k] =  bitArr[k]
    return bitPlaneArr

def intToArray(integer):
    '''
    Convert int to Array
    '''
    array = []
    for digit in (str(integer)):
        array.append(int(digit))
    return array

def encode_block_count(square, blockCount):
    '''
    Encode block count into a matrix
    '''
    binQueueSize = int('{0:b}'.format(blockCount))
    lengthArray = intToArray(binQueueSize)
    queueLength = len(lengthArray)
    xLength = len(square)
    yLength = len(square)
    square = np.zeros((xLength, yLength), dtype='uint8')
    counter = 0

    for i in range(xLength-1, -1, -1):
        for j in range (yLength-1, -1, -1):
            if(counter < queueLength):
                square[i,j] = lengthArray[queueLength - counter -1]
                counter += 1
    return square

def encode(bitPlaneArr, secretArr, alpha):
    '''
    Embed a secretfile (as an array) into vessel (as an array of bit planes)
    '''
    xLength = len(bitPlaneArr)
    yLength = len(bitPlaneArr[0])
    zLength = len(bitPlaneArr[0][0])
    blockCount = len(secretArr[0][0])
    counter = 0

    k=zLength-1
    while(k > -7): #This loop runs through each least significant bit plane before going up
        if(k < 0): #TODO: make this method readable by humans
            k += 31
        for i in range(xLength/9):
            for j in range(yLength/9):
                square = bitPlaneArr[slice(i*9,i*9+9), slice(j*9,j*9+9), k]
                if(counter-1 < blockCount and complexity(square) > alpha):
                    if(counter == 0):
                        square[slice(0,8), slice(0,8)] = encode_block_count(square[slice(0,8),slice(0,8)], blockCount)
                    else:
                        square[slice(0,8), slice(0,8)] = secretArr[:,:,counter-1]
                    square[8,8] = 0
                    if(complexity(square) < alpha):
                        square = array_xor(square)
                        square[8,8] = 1

                    bitPlaneArr[slice(i*9,i*9+9), slice(j*9,j*9+9), k] = square
                    counter += 1
        k -= 8
    return bitPlaneArr

def bin_array_to_decimal(array):
    '''
    Converts a binary array to an int, used for decoding block counts
    '''
    val = 0
    length = len(array)
    for i in range(length):
        val += pow(2,length-i-1)*array[i]
    return int(val)

def decode_block_count(square):
    '''
    Decode block count embedded in matrix
    '''
    rav = square.ravel()
    deci = bin_array_to_decimal(rav)
    return deci

def decode(bitPlaneArr, alpha):
    '''
    Removes file from vessel.
    '''
    xLength = len(bitPlaneArr)
    yLength = len(bitPlaneArr[0])
    zLength = len(bitPlaneArr[0][0])
    blockCount =  1 
    secretArr = [] 
    counter = 0
    marker = False

    k=zLength-1
    while(k > -7):
        if(k < 0):
            k += 31
        for i in range(xLength/9):
            for j in range(yLength/9):
                square = bitPlaneArr[slice(i*9,i*9+9), slice(j*9,j*9+9), k]
                if(counter < blockCount and complexity(square) > alpha):
                    if(square[8,8] == 1):
                        square = array_xor(square)
                    if(counter == 0 and marker == False):
                        blockCount = decode_block_count(square[slice(0,8),slice(0,8)])
                        secretArr = np.zeros((8,8,blockCount), dtype = 'uint8')
                        marker = True
                        continue
                    secretArr[:,:,counter] = square[slice(0,8), slice(0,8)]
                    counter += 1
        k -= 8
    return secretArr

def ImageStack(bitPlaneArr):
    '''
    Convert an array of bit planes into an array of ints
    '''
    array = np.zeros((bitPlaneArr.shape[0], bitPlaneArr.shape[1], 4), dtype = 'uint8')
    for i in range(bitPlaneArr.shape[0]):
        for j in range(bitPlaneArr.shape[1]):
            for k in range(4):
                array[i,j,k] = np.packbits(cgc_to_pbc(bitPlaneArr[i,j,slice(k*8,(k*8)+8)]))
    return array