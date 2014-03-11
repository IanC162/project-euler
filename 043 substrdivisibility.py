#Problem: compute the sum of all 0-9 pandigital numbers w/ substr prime div.

from itertools import permutations

numbers = [''.join(k) for k in permutations('1234567890')]

total = 0

def isDiv(i):
    j = i
    if not int(j[1:4]) % 2 == 0: return False
    if not int(j[2:5]) % 3 == 0: return False
    if not int(j[3:6]) % 5 == 0: return False
    if not int(j[4:7]) % 7 == 0: return False
    if not int(j[5:8]) % 11 == 0: return False
    if not int(j[6:9]) % 13 == 0: return False
    if not int(j[7:10]) % 17 == 0: return False
    return True

for i in numbers:
    if isDiv(i): total += int(i)

print total
raw_input()
