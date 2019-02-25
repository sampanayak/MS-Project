import csv
import pandas as pd
import socket
from urllib.parse import urlparse
contents = []
df = pd.read_csv('top500.pages.05.18.txt')
fileIp = open("IPaddress.txt", "w")
file = open("pathKeyword.txt", "w")
with open('top500.pages.05.18.txt', 'r+') as filehandle:
	df = pd.read_csv('top500.pages.05.18.txt')
	for line in filehandle:
		o = urlparse(line)
		
		#print(o)
		print(o.netloc)
		print(o.path)
		#print(socket.gethostbyname(o.netloc))
		#s = pd.Series(socket.gethostbyname(o.netloc))
		#print(s)
		#df['IP'] = socket.gethostbyname(o.netloc)
		#df['Keywords'] = ((o.path).split("/"))
		#print(df['keywords'])
		file.write(o.path)
		fileIp.write(o.netloc)
	
	#df.to_csv('urls.csv', sep=',', index = False)

'''
c1 = []	
with open('urls.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		c1.append(column[2])
		
print(c1)'''
	
		
		
#filehandle.close()
file.close()


#df['Date'] = '02/2016'
   #df.to_csv(f, sep=',', index=False) 
#file1 = open("splitKeyword.txt", "w")
'''
with open("keyword.txt", "r+") as f:
	 for line in f:
	 	for word in line.split("/"):
	 		print(word)'''
	 		
#file1.close()
	 		
	 	