#Problem: compute the sum of all numbers that cannot be written as a sum
#         of two abundant numbers

abund = []
sums = [False] * 28124

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

for i in range(0, 28123):
    if sumdivisors(i) > i:
        abund.append(i)

for i in range(0,len(abund)):
    for j in range(i,len(abund)):
        if abund[i] + abund[j] <= 28123:
            sums[abund[i] + abund[j]] = True
        else:
            break

total = 0
for a in range(0,len(sums)):
    if not sums[a]:
        total += a

print total
raw_input()
