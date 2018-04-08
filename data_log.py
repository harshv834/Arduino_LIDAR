import serial
import re
import numpy as np
import sys
from matplotlib import pyplot


def main():
	length = int(sys.argv[1])
	port = str(sys.argv[2])
	output = str(sys.argv[3])
	baud = int(sys.argv[4])

	ser = serial.Serial(port,baud)
	
	data =[]
	while(len(data) < length):
		print(len(data))
		data.append(ser.readline())
	
	arr = np.zeros((length,2))
	for i in range(length):
		word = data[i]
		if(len(word)>0):
			seq = map(int,re.findall(r'\d+',word))
			if(len(seq)>0):	
				arr[i][0] = seq[0]
				arr[i][1] = seq[1]
	
	fig = pyplot.figure()
	ax = fig.add_subplot(111,polar=True)
	arr = arr[~(arr==0).all(1)]
	arr[:,1] = np.pi*arr[:,1]/180.0
	arr[:,0] = arr[:,0]+2
	ax.scatter(arr[:,1],arr[:,0])
	np.savetxt(output+'.npy',arr)
	pyplot.show()

if __name__ == '__main__':
	main()
	



