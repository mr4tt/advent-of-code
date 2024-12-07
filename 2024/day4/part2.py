xmasCount = 0
xmas = []
with open("input.txt", "r+") as file1:
    for line in file1:
        xmas.append(line.strip())

diagonal1 = [(-1, -1), (1, 1)]
diagonal2 = [(-1, 1), (1, -1)]

# letter to find, currCoordinates
def findMAS(x, y):
    global xmasCount
    
    first = ()
    second = ()

    # validate first diagonal
    for diag in diagonal1:
        a, b = diag
        if not valid(x + a, y + b): return
        first.add(xmas[a + x][b + y])
    if not ("M" in first and "S" in first): return

    # validate second diagonal 
    for diag in diagonal2:
        a, b = diag
        if not valid(x + a, y + b): return
        second.add(xmas[a + x][b + y])
    if not ("M" in second and "S" in second): return
    
    xmasCount += 1

def valid(x, y):
    return x < len(xmas) and y < len(xmas[0]) and x >= 0 and y >= 0

for x in range(len(xmas)):
    for y in range(len(xmas[0])):
        if xmas[x][y] == "A": findMAS(x, y)

print(xmasCount)