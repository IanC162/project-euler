#Problem: compute the sum of name scores in a text file, where:
#         name score = alphabetical position * sum of letter positions

import string

total = 0

def namescore(name, index):
    total = 0
    for char in name.lower():
        total += string.lowercase.index(char) + 1
    return total * index

with open("reference/namescores.txt","r") as f:
    k = sorted(f.read().split('","'))
    for n in k:
        total += namescore(n, k.index(n)+1)

print total
raw_input()
