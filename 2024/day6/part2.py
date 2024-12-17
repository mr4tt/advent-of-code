file = open("input.txt").read().splitlines()

seenCoord = set()

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
nextDirection = {"^": ">", ">": "v", "v": "<", "<": "^"}

# find our starting point
for i in range(len(file)):
    for j in range(len(file[0])):
        if file[i][j] in directions.keys():
            x = int(i)
            y = int(j)

def navigate(x, y, direction, file):
    # track spots + direction to check for loops
    seen = set()
    while True:
        changeX, changeY = directions[direction]
        while True:
            newX = x + changeX
            newY = y + changeY

            # if out of bounds, the guard is out! 
            if not valid(newX, newY): return 0

            # if we end up in the same spot, we've looped!
            if (newX, newY, direction) in seen: return 1

            # keep going if there's no obstacle
            # otherwise, we break to change direction
            if file[newX][newY] != "#":
                x, y = newX, newY

                seenCoord.add((x, y))
                seen.add((x, y, direction))
            else:
                direction = nextDirection[direction]
                break

def valid(x, y):
    return x < len(file) and y < len(file[0]) and x >= 0 and y >= 0

navigate(x, y, file[x][y], file)
seen2 = seenCoord.copy()

# for each coordinate on the original path, try putting an obstacle there 
# and check if there's a loop
ans = 0
for a, b in seen2:
    newFile = file.copy()
    newFile[a] = newFile[a][:b] + "#" + newFile[a][b + 1:]
    ans += navigate(x, y, file[x][y], newFile)

print(ans)