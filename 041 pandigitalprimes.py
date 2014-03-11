#Problem: compute the greatest pandigital prime

from itertools import permutations
import math

pandigitals = []

def is_prime(n):
    if n <= 2:
        return False
    if not n & 1:
        return False
    for x in range(3,int(n**0.5)+1,2):
        if n%x == 0:
            return False
    return True

out = 0

def pan(length):
    return ([int(''.join(l)) for l in list(permutations('123456789'[:length],length))])

for i in [4,7]:
    pandigitals.extend(pan(i))

for i in pandigitals:
    if is_prime(i) and i > out:
        out = i

print out
raw_input()
