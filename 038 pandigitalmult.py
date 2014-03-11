#Problem: compute the largest 9-pandigital number from concat

current = 0

def concat(a,b):
    return int(str(a)+str(b))

def pandigital(n):
    num = sorted(''.join(str(n)))

    if len(num) != 9:
        return False

    for i in range(len(num)):
        if str(i+1) != str(num[i]):
            return False
    return True

for i in range(1,9999):
    counter, num = 1, i
    while len(str(num)) < 9:
        counter += 1
        num = concat(num,num*counter)
    if len(str(num)) > 9: continue
    if pandigital(num) and (num > current): current = num

print current
raw_input()
