#Problem: compute the smallest number divisble (a(mod b)=0) by all counting numbers 1-20

from fractions import gcd    

def lcmInt(a, b):
    return (a*b)/gcd(a,b)

def lcm(lst):
    i = 0
    j = 1
    while i < len(lst):
        j = lcmInt(j, lst[i])
        i += 1
    return j

print lcm(range(1,21))
raw_input()

