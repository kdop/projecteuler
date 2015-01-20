import math

a = 4 # no of seq. unmbers
m = 0 # largest num

# file to two dimensional int list
numlist = [map(int, line.split()) for line in open('./data.txt')]

# horizontal
for r in range(0, len(numlist)):
	for c in range(0, len(numlist[0]) - (a-1)):
		tmp = 1
		for shift in range(0, a):
			tmp *= numlist[r][c + shift]
		if tmp > m:
			m = tmp

# vertical
for c in range(0, len(numlist[0])):
	for r in range(0, len(numlist) - (a-1)):
		tmp = 1
		for shift in range(0, a):
			tmp *= numlist[r + shift][c]
		if tmp > m:
			m = tmp

for i in range(a-1, 20): # a-1 to skip diagonal length less that a
	for d in range(0, (i+1)-(a-1)): # (i+1)-(a-1) to stop at diagonal length - a
		slashup = 1
		slashlow = 1
		bslashup = 1
		bslashlow = 1
		
		for shift in range (0, a):
			k = d + shift
			slashup *= numlist[k][i-k]
			slashlow *= numlist[19-(i-k)][19-k]
			bslashup *= numlist[k][19-(i-k)]
			bslashlow *= numlist[19-(i-k)][k]
			
		if slashup > m:
			m = slashup
			
		if slashlow > m:
			m = slashlow
		
		if bslashup > m:
			m = bslashup
			
		if bslashlow > m:
			m = bslashlow

print m
