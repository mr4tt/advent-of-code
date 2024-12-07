xmasCount = 0
xmas = []
with open("input.txt", "r+") as file1:
    for line in file1:
        xmas.append(line.strip())

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# given coordinates, find direction of next letter 
def findM(coord):
    global xmasCount
    x, y = coord
    for direction in directions:
        a, b = direction
        if not valid(x + a, y + b): continue
        if xmas[a + x][b + y] == "M" and findAS((a + x, b + y), direction):
            xmasCount += 1

# find other letters 
def findAS(coord, direction):
    x, y = coord
    a, b = direction

    if not valid(x + a, y + b): return False
    if not valid(x + a + a, y + b + b): return False

    return xmas[x + a][y + b] == "A" and xmas[x + a + a][y + b + b] == "S"

def valid(x, y):
    return x < len(xmas) and y < len(xmas[0]) and x >= 0 and y >= 0

for x in range(len(xmas)):
    for y in range(len(xmas[0])):
        if xmas[x][y] == "X": findM((x, y))

print(xmasCount)