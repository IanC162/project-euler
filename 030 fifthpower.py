#Problem: compute the sum of all numbers that are the ^5 of their digits

total = 0

#Woo, O(n)!
for i in range(2,355000):
    if sum([x**5 for x in map(int, str(i))]) == i:
        total += i

print total
raw_input()
