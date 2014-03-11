#Problem: compute the number of distinct terms for powers

k = []

#O(n^2) nested loop
for a in range(2,101):
    for b in range(2,101):
        k.append(a**b)

print len(list(set(k)))
raw_input()
