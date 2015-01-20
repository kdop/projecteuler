import math

def triangleNumber(n):
	if n < 1 or n % 1 != 0:
		return None
		
	summ = 0
	for i in xrange(1,n+1):
		summ += i
		
	return summ
		
def findFactors(n):
	if n < 1 or n % 1:
		return None
		
	factors = []
	
	j = n
	i = 1
	index = 0
	while True:
		if n % i == 0:
			j = n / i
			factors.insert(index, i)
			factors.insert(len(factors)-index, j)
			index += 1
			
		i += 1
			
		if i >= j: # is this faster than sqrt?
			break
	
	return factors
	
n = 1
tnum = 0
f = []
while True:
	tnum = triangleNumber(n)
	f = findFactors(tnum)
	
	if len(f) > 500:
		break
		
	n += 1
		
print f
print tnum
print n
