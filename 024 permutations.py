#Problem: compute the 1,000,000th lexicographic permutation of 0-9

from itertools import permutations

print [int(''.join(p)) for p in permutations("0123456789")][1000000]
raw_input()
