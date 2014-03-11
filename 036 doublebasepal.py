#Problem: compute the sum of all n < 1000000 for which n is a palindrome
#         in bases 2 and 10... python loves this one <3

total = 0

for i in range(0,1000000):
    if (str(i)[::-1] == str(i)) and (bin(i)[2:][::-1] == bin(i)[2:]):
        total += i

print total
raw_input()
