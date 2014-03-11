#Problem: compute the greatest possible sum over a path down a 15line triangle

rows = []

with open("reference/triangle15.txt","r") as f:
    for line in f.readlines():
        rows.append([int(z) for z in line.replace('\n','').split(' ')])

for i,j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:
    rows[i][j] += max([rows[i+1][j],rows[i+1][j+1]])

print rows[0]
raw_input()
