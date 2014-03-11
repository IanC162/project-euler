#Problem: compute the sum of all amicable numbers < 10000

divs = {}
total = 0

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def sumdivisors(n):
    total = 1
    dict_ = {}
    p = prime_factors(n)
    for i in list(set(p)):
        dict_[i] = p.count(i)
    for p in dict_:
        total *= ((p**(dict_[p]+1))-1)/(p-1)
    return total - n

def amicable(a, divs):
    for b in range(1,10000+1):
        if (a == divs[b]) and (b == divs[a]) and (not a == b):
            return True
    return False

for i in range(1,10000+1):
    divs[i] = sumdivisors(i)

for i in range(1,10000+1):
    if amicable(i, divs): total += i

print total
raw_input()
