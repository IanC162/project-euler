#Problem: compute the greatest palindrome that is a product of two 3-digit #s

def palindrome(n):
    return int(str(n)[::-1]) == n

dromes = []

for b in range(100,1000):
    for a in range(b+1,1000):
        if palindrome(a * b):
            dromes.append(a * b)

print max(dromes)
raw_input()

