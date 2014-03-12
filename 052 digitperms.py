#Problem: compute the first n so that 2n,3n...6n all have the same digits

from itertools import permutations

i = 1

while True:

    i += 1
    #print i," ",int(str(i)[0])

    if int(str(i)[0]) > 1: continue
    if int(str(i)[1]) > 6: continue

    p = [int(''.join(x)) for x in permutations(str(i))]
    
    if (2*i in p \
    and 3*i in p \
    and 4*i in p \
    and 5*i in p \
    and 6*i in p ):
        break
    
print i
raw_input()
