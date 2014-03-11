#Problem: compute the sum of all n
#         for which the sum of the factorials of the digits == n

from math import factorial

total = 0

def sumdigfact(n):
    return sum([factorial(x) for x in [int(digit) for digit in str(n)]])

for i in range(3,100000):
    if sumdigfact(i) == i: total += i

print total
raw_input()
