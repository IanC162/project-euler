#Problem: compute a 4-digit series where all terms are permutations of one
#         another, and also prime

from itertools import permutations

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

primes = eras(10000)

perms = []

cntr = 0

for p in primes:
    if not len(str(p)) == 4:
        cntr += 1

primes = primes[cntr:]

for p in primes:
    perms_ = list(set([int(''.join(x)) for x in permutations(str(p))]))
    perms_.remove(p)
    temp = []
    count = 0
    for perm in perms_:
        if perm in primes:
            temp.append(perm)
            count += 1
            if len(temp)==3 and not (temp[0] == temp[1]):
                perms.append(temp)
                
for p in range(0,len(perms)):
    if not (perms[p][2] - perms[p][1] == perms[p][1] - perms[p][0]):
        perms[p] = []
        
while [] in perms: perms.remove([])

print str(perms[0][0])+str(perms[0][1])+str(perms[0][2])
raw_input()
