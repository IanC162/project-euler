#Problem: compute the number of English words in a text file that have
#         a triangular "score"

import string
count = 0

def gettriangulars(n):
    out = []
    count = 1
    while True:
        k = int(count*(count+1)*0.5)
        if k >= n:
            return out
        out.append(k)
        count += 1

with open("reference/trianglewords.txt","r") as f:
    out = [sum([string.uppercase.index(n)+1 for n in m]) for m in f.read().split('","')]

tri = gettriangulars(max(out)+1)

for i in out:
    if i in tri: count += 1

print count
raw_input()
