#Problem: compute the greatest prime < 1000000 that can be written as a sum
#         of primes

result = 0
numprimes = 0
i = 0

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

primes = eras(1000000)
cumulative = [0]

for p in range(len(primes)):
    cumulative.append(primes[p] + cumulative[p])

for i in range(len(cumulative)):
    for j in range(i-(numprimes+1),0,-1):
        if cumulative[i] - cumulative[j] > 1000000: break
        if (cumulative[i]-cumulative[j]) in primes:
            numprimes = i-j
            result = cumulative[i]-cumulative[j]

print result
raw_input()


