contents = []
import re
i = 0
with open('gene.txt') as f:
	lines = f.readlines()
	i = 0
	sizeOflines = len(lines)
	while i < sizeOflines:
		print(lines[i])
		i += 1
		for match in re.finditer(lines[i+2], lines[i]):
			print(match.start())
		
	#for i in lines:
		#print(lines[i])
		#i == i++
	#i = 1
	#print(lines[1])
	
	#for i in lines:
		#print(lines[i++])
		#[ m.start() for m in re.finditer(lines[i++], lines[i])]
		#for match in re.finditer(lines[2], lines[1]):
			#print(match.start())

			
			#contents = []
import re
#i = 0
with open('gene.txt') as f:
    lines = f.readlines()
    i = 1
    sizeOflines = len(lines)
    while i < sizeOflines:
        # print(lines[i])
        fullString = lines[i]
        i += 1
        sub = lines[i]
        print(fullString)
        print(sub)
        i += 1
        for match in re.finditer('sub','fullString'):
            print(match.start())
        #[m.start() for m in re.finditer('sub', 'fullString')]

	
	
