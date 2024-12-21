from collections import defaultdict
import math

file = open("input.txt").read().splitlines()

length, width = len(file), len(file[0])
maxDistance = math.sqrt((length * length) + (width * width))

antinodes = set()
nodes = defaultdict(list)

def valid(x, y):
    return x < len(file) and y < len(file[0]) and x >= 0 and y >= 0

# find every antennae
for x in range(length):
    for y, char in enumerate(file[x]):
        if char != ".":
            nodes[char].append((x, y))

# loop thru the grid
# if we find an antennae, find its matching pair, then find the antinode
for x in range(length):
    for y, char in enumerate(file[x]):
        if char != ".":
            for antennae in nodes[char]:
                if antennae != (x, y):
                    x2, y2 = antennae[0], antennae[1]

                    # if two antennae more than half the distance of the grid apart, there's no legal antinode
                    xSqrd = (x - x2) * (x - x2)
                    ySqrd = (y - y2) * (y - y2)
                    distance = math.sqrt(xSqrd + ySqrd)

                    if distance > maxDistance:
                        continue

                    xDiff = x - x2
                    yDiff = y - y2

                    xAnti = x + xDiff
                    yAnti = y + yDiff

                    if valid(xAnti, yAnti): antinodes.add((xAnti, yAnti))

print(len(antinodes))