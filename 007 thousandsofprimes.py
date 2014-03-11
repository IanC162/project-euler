#Problem: compute the 10001st prime number

import math

primes = int(12000 * math.log(12000))

def eras(n):
    a = set(range(2,n+1))
    l = round(n**0.5)
    for i in range(2,int(l+1)):
        if i in a:
            s = i**2
            while s <= n:
                if s in a:
                    a.remove(s)
                s += i
    return list(a)


print eras(primes)[10000]

raw_input()
