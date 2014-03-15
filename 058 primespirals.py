#Problem: compute the first sidelength of a number spiral whose diagonals are
#         less than 10% prime

from math import sqrt

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

slen = 2

diag = 3

c = 9

while (float(diag)/(2*slen+1) > 0.10):
    slen += 2
    for i in range(3):
        c += slen
        if is_prime(c): diag += 1
    c += slen
    
print slen+1
raw_input()

