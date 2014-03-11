#Problem: find sum of primes < 2000000

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

print sum(eras(2000000))

raw_input()
    
