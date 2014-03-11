#Problem: compute the number < 1000000 with the longest Collatz sequence

out = 0
outc = 0

for i in range(1,1000000):
    cntr = 0
    n = i
    while not (n == 1):
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        cntr += 1
    if cntr > outc:
        out = i
        outc = cntr

print out
raw_input()
