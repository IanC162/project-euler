#Problem: compute the sum the even fibanocci numbers up to 4 million

a = 1
b = 1

out = 0

def fib(n):
    a, b = 0, 1

    while b <= n:
        a, b = b, a + b
        if b % 2 == 0: yield b

print sum(fib(4000000))
raw_input()
