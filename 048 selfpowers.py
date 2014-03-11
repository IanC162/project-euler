#Problem: compute sum from i=1 to 1000 of i^i

print str(sum([i**i for i in range(1,1000+1)]))[-10:]
raw_input()
