def schematic(file):
    sum = 0
    schema = []
    with open(file, "r") as input:
        for line in input:
            # remove trailing newline
            schema.append(line.strip())

    for i in range(len(schema)):
        numEndIndex = set()
        for j in range(len(schema[0])):
            if schema[i][j].isdigit():
                itr = 0
                number = ""
                # find when the number stops, itr tracks how long it is
                while True:
                    if j + itr < len(schema[0]) and schema[i][j + itr].isdigit():
                        number += schema[i][j + itr]
                        itr += 1
                    else:
                        break

                # if we've already seen this number, continue
                if j + itr in numEndIndex:
                    continue
                
                # build a box around the number, check if any symbols are inside
                rowStart = i - 1 if i != 0 else 0
                rowEnd = i + 1 if i != len(schema) - 1 else i

                colStart = j - 1 if j != 0 else 0
                colEnd = j + itr if j + itr < len(schema[0]) else len(schema[0]) - 1

                exitFlag = False
                for x in range(rowStart, rowEnd + 1):
                    for y in range(colStart, colEnd + 1):
                        if schema[x][y] != "." and not schema[x][y].isdigit():
                            numEndIndex.add(j + itr)
                            sum += int(number)
                            exitFlag = True
                            break

                    if exitFlag: break

    return sum


# def schematic(file):
#     sum = 0
#     schema = []
#     with open(file, "r") as input:
#         for line in input:
#             # remove trailing newline
#             schema.append(line.strip())
#     print(schema)
#     print(len(schema))
#     print(len(schema[0]))
#     for i in range(len(schema)):
#         for j in range(len(schema[0])):
#             if schema[i][j] != "." or not schema[i][j].isdigit():
#                 rowStart = i - 1 if i != 0 else 0
#                 rowEnd = i + 1 if i != len(schema) - 1 else i

#                 colStart = j - 1 if j != 0 else 0
#                 colEnd = j + 1 if j != len(schema[0]) - 1 else j
#                 print("rows", rowStart, rowEnd)
#                 print("cols", colStart, colEnd)

#                 usedParts = ()
#                 for x in range(rowStart, rowEnd + 1):
#                     for y in range(colStart, colEnd + 1):
#                         #print(x, y)
#                         #print(schema[9][10])

#                         if schema[x][y].isdigit():
#                             sum += int(schema[x][y])
#     return sum

file = "day3_input.txt"
print("ans: ", schematic(file))