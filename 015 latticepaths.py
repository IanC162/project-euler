#Problem: compute the number of paths (not backtracking) from corner to corner
#         on a 20x20 grid

def paths(sx, sy):
    numbers = []
    for n in range(0,sx):
        numbers.append(range(0,sy))

    for x in range(0,sx):
        for y in range(0,sy):
            if (x == 0) or (y == 0):
                numbers[y][x] = 1
            else:
                numbers[y][x] = numbers[y-1][x] + numbers[y][x-1]

    return numbers[sy-1][sx-1]

print paths(21,21)
raw_input()
