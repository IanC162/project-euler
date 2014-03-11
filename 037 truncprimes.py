#Problem: compute the sum of all 11 truncatable primes

lim = 1000000
total = 0
count = 0

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
    return a

primes = eras(lim)

for k in primes:
    if count >= 15:
        break
    r, l, mult = k, 0, 1
    trunc = True
    while (r > 0) and trunc:
        l += mult * (r % 10)
        trunc = (l in primes) and (r in primes)
        r /= 10
        mult *= 10
    if trunc:
        count += 1
        total += k
        
total -= 17
print total
raw_input()
