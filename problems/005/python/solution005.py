import math

def find_factors(number):
    factors = []
    tmp = number
    
    while (True):
        f = 2
        root = math.ceil(math.sqrt(tmp))
        while (f <= root): # If reached root, tmp is prime. <= instead of < to cover if tmp == 4
            if tmp % f == 0:
                #f is a prime factor of tmp
                factors.append(f)
                tmp = tmp / f
                break

            else:
                f += 1
    
        if f >= root: # >= instead of == covers the case when tmp == 1
            factors.append(tmp)
            break
            
    return factors
    
# I used the simple algorithm of braking each number into factors,
# and then multiply the largest occurrence of each factor.
#
# 20 = 2 * 2 * [5]
# 8 = [2 * 2 * 2]
# 9 = [3 * 3]
# LCM = 2 * 2 * 2 * 3 * 3 * 5 = 360

primec = {}
for n in range(1,21):
    f = find_factors(n)
    l = len(f)
    i = 0
    c = 0
    while (i < l):
        c = f.count(f[i])
        if f[i] not in primec or c > primec[f[i]]:
            primec[f[i]] = c
    
        # my find_factors method returs the factors sorted.
        # After we count the number of occurrences go to the next factor. 
        i += c

#print(primec)

r = 1
for key in primec:
    r = r * (key ** primec[key])
    
print(r)
