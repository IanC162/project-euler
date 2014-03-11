#Problem: compute the sum of the digits of 100!

from math import factorial

x = factorial(100)

print sum([int(d) for d in str(x)])
raw_input()
