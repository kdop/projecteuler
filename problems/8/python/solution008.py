with open ("../data.txt", "r") as myfile:
	numstr = myfile.read().replace('\n', '')

digits = list(map(int, numstr)) # string to list of ints

depth = 13 # how many adjacent digits
answer = 0
shift = 0

while shift <= len(digits) - depth:
	m = 1
	for i in range(13): # 0...12
		m *= digits[shift+i]
		
	if m > answer:
		answer = m
	
	shift += 1
		
print answer
