import math

# Python obviously has build-in functions for this. I implemented my own for fun.
def itoa(i):
    digits = []
    
    i = abs(i) # I want to handle only positive.
    
    while (True):
        digits.insert(0, i % 10)
        i = i // 10
        
        if i == 0:
            break
            
    return digits
    
def is_palindrome(i):
    d = itoa(i)
    shift = 0
    l = len(d)
    
    for shift in range(l // 2):
        if d[shift] != d[(l-1)-shift]:
            return False
    
    return True

palindromes = []
for i in range(100,999):
    for j in range(i,999): # Start from i, because i * j == j * i.
        p = i * j
        if is_palindrome(p):
            palindromes.append(p)

print(max(palindromes))
