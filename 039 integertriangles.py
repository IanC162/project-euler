#Problem: compute the number < 1000 with the greatest number of right triangles

r, rs = 0,0

for i in range(2,1000,2):
    sol = 0
    for j in range(2,(i/3)+1):
        if (i**2-(2*i*j)) % (2*(i-j)) == 0:
            sol += 1
    if sol > rs:
        rs = sol
        r = i

print r
raw_input()
