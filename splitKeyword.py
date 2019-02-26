#import re
'''file1 = open("splitedKeyword.txt", "w")
with open("pathKeyword.txt", "r+") as f:
	 for line in f:
	 	for word in line.split("/"):
	 		
file1.write(word)
	 		
file1.close()

with open("splitedKeyword.txt", "r+") as f:
	 for line in f:
	 	for word in line.split("_,.,:, ,-"):
	 		f.write(word)
#file1.close()'''

file = open("testSplitedKeyword.txt", "w")
with open("splitedKeyword.txt") as f:
	content = f.readlines()
	#print(content)
	for lines in content[0].split():
		for split0 in lines.split(' '):
			for split1 in split0.split(','):
				for split2 in split1.split('.'):
					for split3 in split2.split('?'):
						for split4 in split3.split('!'):
							for split5 in split4.split(':'):
								for split6 in split5.split('-'):
									for split7 in split6.split('%'):
										for word in split7.split('_'):
											if word != "":
												print(word)