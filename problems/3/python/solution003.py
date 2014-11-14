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

print(find_factors(600851475143))
