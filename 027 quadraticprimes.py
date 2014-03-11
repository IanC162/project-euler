#Problem: compute the product of the coefficents for the prime-generating quadratic

m = 0
c = 0
d = 0

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

primes = eras(1000)

def checkprimes(a,b):
    k = 1
    while True:
        if (k**2+k*a+b) not in primes: break
        k += 1
    return k

for a in range(-999,1000):
    for b in range(-999,1000):
        k = checkprimes(a,b)
        if k > m:
            m = k
            c, d = a, b

print c*d
raw_input()
