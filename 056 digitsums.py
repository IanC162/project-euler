#Problem: compute the maximum digital sum of n^n for n < 100

print max((sum(int(k) for k in str(a**b)) for a in range(1,100) for b in range(1,100)))
raw_input()
