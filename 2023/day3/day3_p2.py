def schematic(file):
    sum = 0
    schema = []
    with open(file, "r") as input:
        for line in input:
            # remove trailing newline
            schema.append("." + line.strip() + ".")

    schema = ["." * len(schema[0])] + schema + ["." * len(schema[0])]

    for i in range(len(schema) - 1):
        for j in range(len(schema[0]) - 1):
            numbers = []
            if schema[i][j] == "*":
                # looking right 
                if schema[i][j + 1].isdigit():
                    itr = 1
                    currNum = ""
                    while schema[i][j + itr].isdigit():
                        currNum += schema[i][j + itr]
                        itr += 1
                    numbers.append(currNum)

                # looking left
                if schema[i][j - 1].isdigit():
                    itr = 1
                    currNum = ""
                    while schema[i][j - itr].isdigit():
                        currNum = schema[i][j - itr] + currNum
                        itr += 1
                    numbers.append(currNum)

                # looking top left
                topLeftFlag = False
                if schema[i - 1][j - 1].isdigit():
                    print("a" + schema[i - 1][j - 1])

                    topLeftFlag = True
                    itr = 1
                    topLeftNum = ""
                    while schema[i - 1][j - itr].isdigit():
                        topLeftNum = schema[i - 1][j - itr] + topLeftNum
                        itr += 1
                        print("topleft", topLeftNum)
                    
                # looking top right
                topRightFlag = False
                if schema[i - 1][j + 1].isdigit():
                    topRightFlag = True
                    itr = 1
                    topRightNum = ""
                    while schema[i - 1][j + itr].isdigit():
                        topRightNum += schema[i - 1][j + itr]
                        itr += 1

                # looking up 
                up = schema[i - 1][j]
                if up.isdigit():
                    if topRightFlag and topLeftFlag:
                        numbers.append(topLeftNum + up + topRightNum)
                    elif topRightFlag:
                        numbers.append(up + topRightNum)
                    elif topLeftFlag:
                        numbers.append(topLeftNum + up)
                    else:
                        numbers.append(up)
                else:
                    if topRightFlag:
                        numbers.append(topRightNum)
                    if topLeftFlag:
                        numbers.append(topLeftNum)

                # looking bottom left
                bottomLeftFlag = False
                if schema[i + 1][j - 1].isdigit():
                    bottomLeftFlag = True
                    itr = 1
                    bottomLeftNum = ""
                    while schema[i + 1][j - itr].isdigit():
                        bottomLeftNum = schema[i + 1][j - itr] + bottomLeftNum
                        itr += 1

                # looking bottom right
                bottomRightFlag = False
                if schema[i + 1][j + 1].isdigit():
                    bottomRightFlag = True
                    itr = 1
                    bottomRightNum = ""
                    while schema[i + 1][j + itr].isdigit():
                        bottomRightNum += schema[i + 1][j + itr]
                        itr += 1

                # looking down
                down = schema[i + 1][j]
                if down.isdigit():
                    if bottomRightFlag and bottomLeftFlag:
                        numbers.append(bottomLeftNum + down + bottomRightNum)
                    elif bottomRightFlag:
                        numbers.append(down + bottomRightNum)
                    elif bottomLeftFlag:
                        numbers.append(bottomLeftNum + down)
                    else:
                        numbers.append(down)
                else:
                    if bottomRightFlag:
                        numbers.append(bottomRightNum)
                    if bottomLeftFlag:
                        numbers.append(bottomLeftNum)

                if len(numbers) != 2:
                    continue
                else:
                    sum += int(numbers[0]) * int(numbers[1])

    return sum

file = "day3_input.txt"
print("ans: ", schematic(file))