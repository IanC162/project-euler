#Problem: compute maximum prime factor of 600,851,475,143

import math

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

print max(prime_factors(600851475143))

raw_input()
