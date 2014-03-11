#Problem: compute the longest reciprocal cycle of 1/n, n < 1000

m = 0
n = 0

def cycle(n):
    found = []
    total = 0
    k = 1
    while k not in found:
        found.append(k)
        k *= 10
        k %= n
        total += 1
    return total

for p in range(1,1000):
    k = cycle(p)
    if k > m:
        m = k
        n = p

print "Number: " + str(n)
print "Cycles: " + str(m)
raw_input()
