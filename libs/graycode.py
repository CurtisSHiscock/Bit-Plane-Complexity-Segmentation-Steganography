def pbc_to_cgc(arr):
	'''
	Convert pure binary code to canonical gray code
	'''
	for i in range (len(arr)-2,0,-1):
		arr[i] = (arr[i] ^ arr[i-1])
	return arr

def cgc_to_pbc(arr):
	'''
	Convert canonical gray code to pure binary code
	'''
	for i in range(1, len(arr)-1, +1):
		arr[i] = arr[i] ^ arr[i-1]
	return arr