"""import csv
import pandas as pd
df = pd.read_csv('splitKeyword.csv')
print (df)
document = df.values.tolist()
print(document)"""

"""import csv
with open('splitKeyword.csv', 'r') as f:
	reader = csv.reader(f)
	my_list = list(reader)
print (my_list)"""

fo = open("keyword.txt", "r")
item = fo.readlines()
print(item)