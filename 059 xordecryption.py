#Problem: decrypt an XOR-encoded file via brute force

import string

content = []

def isenglish(s):
    return s.split(" ").count("the") > 1

def decrypt(c, s):
    s = s * (len(c)/3 + 1)
    k = 0
    out = ""
    for num in c:
        out += chr(int(num) ^ ord(s[k]))
        k += 1
    return out
        
def finish(s):
    print sum(ord(l) for l in s)
    raw_input()
    exit()

with open("reference/xordecryption.txt","r") as f:
    content = f.read().split(',')

for l1 in string.ascii_lowercase:
    for l2 in string.ascii_lowercase:
        for l3 in string.ascii_lowercase:
            s = l1+l2+l3
            if isenglish(decrypt(content, s)):
                finish(decrypt(content, s))
    
print "found no matches"
raw_input()
