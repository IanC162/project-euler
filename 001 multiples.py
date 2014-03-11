#Problem: compute the sum of multiples of 3 and 5 for numbers less than 1000

x = 1

out = 0

while x < 1000:
    if (x % 3 == 0) or (x % 5 == 0):
        out += x
    x += 1

print str(out)
raw_input()
