#Problem: compute the lowest difference pentagonal numbers which add/sub to P_n

from itertools import combinations
from math import *
from operator import *

found = False

def pentagonal(n):
    return n*(3*n-1)/2

pentagonals = set(pentagonal(n) for n in range(1, 3000))
c = combinations(pentagonals, 2)
for p in c:
    if add(*p) in pentagonals and abs(sub(*p)) in pentagonals:
        print abs(sub(*p))

raw_input()
    
