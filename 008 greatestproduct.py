#Problem: compute the greatest product of five consecutive digits in a series

import math

with open("reference/greatestproduct.txt","r") as f:
    s = f.read()
lst = []

for i in range(0, len(s)-5):
    c0 = int(s[i])
    c1 = int(s[i+1])
    c2 = int(s[i+2])
    c3 = int(s[i+3])
    c4 = int(s[i+4])

    lst.append(c0*c1*c2*c3*c4)

print max(lst)

raw_input()
