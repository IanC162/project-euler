#Problem: compute the product of digits of the concatenation of natural #s

lim = 500000

s = ''.join([str(x) for x in range(1,lim+1)])

print int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999])
raw_input()
