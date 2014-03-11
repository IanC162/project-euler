#Problem: compute the least odd composite number that cannot be written in
#         a form P_a+2b^2

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

def isTwiceSqr(n):
    o = (n/2.0)**0.5
    return o == int(o)

#if is twice square, return true
def isResult(n):
    for j in primes:
        if j >= n: return False
        if isTwiceSqr(n - j): return True

primes = list(eras(10000))
oddcomp = []

total = 1
found = False

for i in range(3,10000,2):
    if not (i in primes):
        oddcomp.append(i)

for i in oddcomp:
    if not isResult(i):
        total = i
        break
        

print total
raw_input()
