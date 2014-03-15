#Problem: compute the number of "Lychrel numbers" < 10,000

count = 0

for k in range(1,10000):
    l = k
    l += int(str(l)[::-1])
    cntr = 1
    while not (l == int(str(l)[::-1])):
        cntr += 1
        l += int(str(l)[::-1])
        if cntr > 50:
            count += 1
            break

print count
raw_input()
    
