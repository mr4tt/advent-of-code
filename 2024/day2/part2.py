ans = 0

# check if list of nums are correct
def checker(line):
    levelType = ""
    prevChar = line[0]
    for n in range(1, len(line)):
        if abs(line[n] - prevChar) <= 3 and abs(line[n] - prevChar) >= 1:
            if levelType == "":
                levelType = True if line[n] - prevChar < 0 else False
            elif (levelType and line[n] - prevChar > 0) or (not levelType and line[n] - prevChar < 0):
                return False
        else:
            return False
        prevChar = line[n]

    return True

with open("input.txt", "r+") as file1:
    for line in file1:
        line = line.split(" ")
        line = [int(num) for num in line]

        index = checker(line)
        # if list of nums aren't correct, try systemetically removing each one and checking again
        if index == False:
            for n in range(len(line)):
                tempLine = line.copy()
                tempLine.pop(n)
                index = checker(tempLine)
                if index == True:
                    break
        if index:
            ans += 1

print(ans)