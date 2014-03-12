#Problem: find an eight prime replacement family

out = 0

import string
from math import sqrt

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

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def family(n, r):
    total = 0
    for d in '0123456789':
        k = int(string.replace(n,r,d))
        if k>100000 and is_prime(k):
            total += 1
    return total==8

primes = eras(1000000)

for p in primes:
    if p > 100000:
        s = str(p)
        ld = s[5:6]
        if s.count('0') == 3 and family(s,'0') and ld != 0:
            out = int(s)
            break
        if s.count('1') == 3 and family(s,'1') and ld != 1:
            out = int(s)
            break
        if s.count('2') == 3 and family(s,'2') and ld != 2:
            out = int(s)
            break

print out
raw_input()

        
        
    
