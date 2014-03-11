#Problem: compute the difference of sum of squares and square of sum for integers 1 to 100

import math

def sqr(lst):
    out = []
    for k in lst:
        out.append(k**2)
    return out

print abs((sum(range(1,101)))**2-sum(sqr(range(1,101))))
         
raw_input()
