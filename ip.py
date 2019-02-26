import csv
import pandas as pd
import socket
from urllib.parse import urlparse
contents = []

#read the text file
df = pd.read_csv('top500.pages.05.18.txt')

#open IPaddress.txt file
fileIp = open("IPaddress.txt", "w")

#open pathKeyword.txt file
file = open("pathKeyword.txt", "w")
with open('top500.pages.05.18.txt', 'r+') as filehandle:
	df = pd.read_csv('top500.pages.05.18.txt')
	for line in filehandle:
		o = urlparse(line)
		
		#print(o)
		#print(o.netloc)
		#print(o.path)
		#print(socket.gethostbyname(o.netloc))
		'''s = pd.Series(socket.gethostbyname(o.netloc))
		print(s)'''
		#df1['IP'] = socket.gethostbyname(o.netloc)
		#df['Keywords'] = ((o.path).split("/"))
		#print(df['keywords'])
		#file.write(o.path)
		fileIp.write((socket.gethostbyname(o.netloc)))
		
fileIp.close()