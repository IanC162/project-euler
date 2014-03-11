#Problem: compute the product abc in the pythagorean triple in which a+b+c=1000

def triple():
    for n in range(2,1001):
        for m in range(2,1001):
            if n > m:
                a = n**2 - m**2
                b = 2*m*n
                c = n**2 + m**2
                if a+b+c == 1000:
                    return a*b*c

print triple()
raw_input()


        
