#Problem: compute the sum of all products that make up a 9-digit pandigital

from itertools import permutations

total = 0

def pandigital(n):
    num = sorted(''.join(str(n)))

    if len(num) != 9:
        return False

    for i in range(len(num)):
        if str(i+1) != str(num[i]):
            return False
    return True

def concat(a, b):
    c = b
    while c > 0:
        a *= 10
        c /= 10
    return a + b

pan = set()

for i in range(1,5000):
    for j in range(1,100):
        if pandigital(concat(i,concat(j,i*j))):
            pan.add(i*j)

print sum(pan)
raw_input()
