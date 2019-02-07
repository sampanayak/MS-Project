import socket
from urllib.parse import urlparse
#contents = []
with open('urls.txt', 'r') as filehandle:
	for line in filehandle:
		o = urlparse(line)
		#print(o)
		print(o.netloc)
		print(socket.gethostbyname(o.netloc))
		
filehandle.close()
		
