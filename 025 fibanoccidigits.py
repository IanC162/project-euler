#Problem: compute the first fibanocci term number to have 1000 digits

count = 0

a = 0
b = 1

while True:
    a, b = b, a + b
    count += 1
    if len(str(a)) >= 1000:
        break

print count
raw_input()
