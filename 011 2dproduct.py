#Problem: compute the greatest product of a row/diagonal in a 2d grid of #s

data = []
greatest = 0

with open("reference/2dproduct.txt","r") as f:
    for line in f.readlines():
        data.append([int(i) for i in line[:-1].split(' ')])

def checkProducts(x,y):
    global greatest
    
    n = get(x,y) * get(x+1,y) * get(x+2,y) * get(x+3,y)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x-1,y) * get(x-2,y) * get(x-3,y)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x,y+1) * get(x,y+2) * get(x,y+3)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x,y-1) * get(x,y-2) * get(x,y-3)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x+1,y+1) * get(x+2,y+2) * get(x+3,y+3)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x+1,y-1) * get(x+2,y-2) * get(x+3,y-3)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x-1,y-1) * get(x-2,y-2) * get(x-3,y-3)
    if n > greatest:
        greatest = n
    n = get(x,y) * get(x-1,y+1) * get(x-2,y+2) * get(x-3,y+3)
    if n > greatest:
        greatest = n

def get(x,y):
    try:
        return data[y][x]
    except IndexError:
        return 0

for x in range(0,20):
    for y in range(0,20):
        checkProducts(x,y)

print greatest
raw_input()
