#Problem: compute the number of iterations of continued frac. of root 2
#         whose numerator has more digits than its denominator

n, d, count = 2, 3, 0

for k in range(1000):
    if len(str(n)) > len(str(d)): count += 1
    last = n
    n += 2*d
    d += last

print count
raw_input()

