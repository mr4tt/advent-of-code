def schematic(file):
    sum = 0
    schema = []
    with open(file, "r") as input:
        for line in input:
            # remove trailing newline
            schema.append("." + line.strip() + ".")

    schema = ["." * len(schema[0])] + schema + ["." * len(schema[0])]
    
    # ensure we don't use the same number / gear again
    numEndIndex = set()
    for i in range(len(schema) - 1):
        for j in range(len(schema[0]) - 1):
            numbers = []
            if schema[i][j] == "*":        
                rowStart = i - 1 if i != 0 else 0
                rowEnd = i + 1 if i != len(schema) - 1 else i

                colStart = j - 1 if j != 0 else 0
                colEnd = j + 1 if j != len(schema[0]) - 1 else j

                # make a box around the * to check for numbers
                for x in range(rowStart, rowEnd + 1):
                    for y in range(colStart, colEnd + 1):   
                        if schema[x][y].isdigit():
                            currNum = schema[x][y]
                            leftItr, rightItr = 1, 1

                            # find digits to the left and right
                            while schema[x][y - leftItr].isdigit():
                                currNum = schema[x][y - leftItr] + currNum
                                leftItr += 1
                            while schema[x][y + rightItr].isdigit():
                                currNum += schema[x][y + rightItr]
                                rightItr += 1

                            # decrement iterators bc after the while loop, they are 1 over
                            rightItr -= 1
                            leftItr -= 1
                            
                            # check if we've used this gear already
                            if (x, y + rightItr) not in numEndIndex:
                                numEndIndex.add((x, y + rightItr))
                            else:
                                continue
                            numbers.append(currNum)

                if len(numbers) != 2:
                    continue

                sum += int(numbers[0]) * int(numbers[1])
    return sum

file = "day3_input.txt"
print("ans: ", schematic(file))