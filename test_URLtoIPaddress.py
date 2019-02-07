#urls to keywords
#import csv
from urllib.parse import urlparse

contents = []
f = open('urls.txt', 'r')
urls = f.read()
print(urls)
for url in urls:
	contents.append(url)
	print(contents)
	url_keyword = urlparse(url)
	#print(url_keyword)
#f.close()		

#input
#output
#ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')

#Convert hostname to IP address
#import socket
#print(socket.gethostbyname('google.com'))

