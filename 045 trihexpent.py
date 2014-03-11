#Problem: compute the second hexagonal number that is also triangular & pent.

i, j = 143, 0

def isPent(x):
    y = ((24.0*x+1)**0.5+1)/6.0
    return y == int(y)

while True:
    i += 1
    j = i * (2*i-1)
    if isPent(j): break

print j
raw_input()
