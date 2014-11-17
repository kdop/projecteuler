import sys
import math

# in order to be a < b < c,
#	a < 333
#	b < 500

for a in range(1, 333):
	for b in range(a+1, 500):
		c = math.sqrt(a*a + b*b)
		if c == 1000 - (a + b):
			print(a * b * c)
			sys.exit(1)
