#complexity.py
import numpy as np
## Methods for determining complexity of squares

def checkerboard(shape):
    '''
    returns a checkerboard
    '''
    return np.indices(shape).sum(axis=0) % 2

def array_xor(array):
    '''
    returns XOR of an array and a checkberboard of the same shape
    '''
    checker = checkerboard(array.shape)
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i,j] = array[i,j] ^ checker[i,j]
    return array

def complexity(matrix):
    '''
    calculates complexity of square
    '''
    maxComplexity = 81.0
    complexity = 1.0
    previous = matrix[0,0]

    try:
        assert(matrix.shape == (9,9))
    except:
        print("Error in complexity(). Expected (9,9) matrix. Received: " + str(matrix.shape))

    for i in range(0,9):
        for j in range(0,9):
            if(i == 8 and j == 8): #Ignore final square - which we use to see if we have XORed a square
                continue
            if(matrix[i,j] != previous):
                complexity += 1
            previous = matrix[i,j]
    return complexity/maxComplexity

def capacity(bitPlaneArr, alpha):
    '''
    Iterates through the bitplane with our traversal loop, incrementing a counter when it encounters a block
    meeting the complexity threshold.

    Returns number of possible blocks we can store in this vessel
    '''
    xLength = len(bitPlaneArr)
    yLength = len(bitPlaneArr[0])
    zLength = len(bitPlaneArr[0][0])
    counter = 0

    for k in range(zLength-1,-1,-1):
        for i in range(xLength/9):
            for j in range(yLength/9):
                square = bitPlaneArr[slice(i*9,i*9+9), slice(j*9,j*9+9), k]
                if(complexity(square) > alpha):
                    counter+=1
    return counter

def verifyCapacity(vessel, secret, alpha):
    '''
    Compares capacity of vessel at alpha vs the number of squares we're embedding
    '''
    return capacity(vessel, alpha) > len(secret[0][0])