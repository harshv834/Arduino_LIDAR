import serial
import re
import numpy as np
import sys

def main():
	length = int(sys.argv[1])
	port = str(sys.argv[2])
	output = str(sys.argv[3])
	baud = int(sys.argv[4])

	ser = serial.Serial(port,baud)
	
	data =[]
	while(len(data) < length):
		data.append(ser.readline())
	
	arr = np.zeros(length,2)
	for i in range(length):
		word = data[i]
		s1 = re.search(',',word)
		s2 = re.search('\r',word)
		arr[i][0] = int(word[0:s1])
		arr[i][1] = int(word[s1+1:s2])
	
	np.savetxt(output+'.npy',arr)

if __name__ == '__main__':
	main()
	



