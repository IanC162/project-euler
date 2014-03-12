#Problem: compute the number of combinations (n choose k), where n <= 100,
#         k <= 100, and n choose k > 1000000

from math import factorial

count = 0

for n in range(1,101):
    for k in range(1,n+1):
        if float(factorial(n)) / float(factorial(k)*factorial(n-k)) > 1000000:
            count += 1

print count
raw_input()
