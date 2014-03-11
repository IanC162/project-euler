#Problem: compute the first triangular number with at least 500 divisors

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

def divisors(n):
    factors = prime_factors(n)
    unique = list(set(factors))
    prod = 1

    for u in unique:
        prod *= factors.count(u)+1

    return prod

i = 0

while True:
    n = i*(i+1)/2
    if divisors(n) >= 500:
        print n
        raw_input()
        exit()
    else:
        i += 1
