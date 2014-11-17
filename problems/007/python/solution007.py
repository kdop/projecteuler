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
                tmp = math.floor(tmp / f)
                
                # in case numver is 2, the <= in the inner while, makes 1 added as a factor.
                # this if prevents this.
                if (tmp == 1):
                    return factors
                    
                break

            else:
                f += 1
    
        if f >= root: # >= instead of == covers the case when tmp == 1
            factors.append(tmp)
            break
            
    return factors

def first_primes(c):
    if c < 1:
        return None
        
    primes = []
    found = 0
    i = 1
    while found < c:
        if len(find_factors(i)) == 1:
            primes.append(i);
            found += 1
        i += 1
    
    return primes

print(first_primes(10002))
