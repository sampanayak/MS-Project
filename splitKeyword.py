'''file1 = open("splitKeyword.txt", "w")
with open("keyword.txt", "r+") as f:
	 for line in f:
	 	for word in line.split("/"):
	 		file1.write(word)'''
	 		
#file1.close()

file1 = open("pathKeyword.txt", "w")
with open("pathKeyword.txt", "r+") as f:
	 for line in f:
	 	for word in line.split("/"):
	 		file1.write(word)
file1.close()