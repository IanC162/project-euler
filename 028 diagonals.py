#Problem: compute the sum on the diagonals of 500*500 square

total = 1

for x in range(1,501):
    total += 4*((2*x+1)**2)-12*x

print total
raw_input()
