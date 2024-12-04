ans = 0

with open("input.txt", "r+") as file1:
    for line in file1:
        line = line.split(" ")
        line = [int(num) for num in line]
        # True = decreasing, False = increasing
        levelType = ""
        prevChar = line[0]

        flag = True
        for n in range(1, len(line)):
            # if intervals between numbers are correct
            if abs(line[n] - prevChar) <= 3 and abs(line[n] - prevChar) >= 1:
                # if undecided between decreasing or increasing
                if levelType == "":
                    levelType = True if line[n] - prevChar < 0 else False
                # if current numbers don't match previously decided pattern
                elif (levelType and line[n] - prevChar > 0) or (not levelType and line[n] - prevChar < 0):
                    flag = False
            else:
                flag = False
            prevChar = line[n]
        if flag:
            ans += 1

print(ans)