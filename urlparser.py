import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

contents = []
with open('urls.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents

for url in contents:  # Parse through each url in the list.
    page = urlopen(url[0]).read()
    soup = BeautifulSoup(page, "html.parser")
print(soup)