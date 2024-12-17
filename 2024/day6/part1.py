file = open("input.txt").read().splitlines()

seen = set()

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
nextDirection = {"^": ">", ">": "v", "v": "<", "<": "^"}

# find our starting point
for i in range(len(file)):
    for j in range(len(file[0])):
        if file[i][j] in directions.keys():
            x = int(i)
            y = int(j)

# include the current tile 
seen.add((x, y))

def navigate(x, y, direction):
    while True:
        changeX, changeY = directions[direction]
        while True:
            newX = x + changeX
            newY = y + changeY

            # if out of bounds, then the guard is out! 
            if not valid(newX, newY): return

            # keep going if there's no obstacle
            # otherwise, we break to change direction
            if file[newX][newY] != "#":
                x, y = newX, newY

                seen.add((x, y))
            else:
                direction = nextDirection[direction]
                break

def valid(x, y):
    return x < len(file) and y < len(file[0]) and x >= 0 and y >= 0

navigate(x, y, file[x][y])

print(len(seen))