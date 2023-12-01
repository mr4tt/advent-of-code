input = "day3\\input3.txt"
priorities = 0
with open(input, "r") as fp:
    for line in fp:
        firstHalf = set(line[:len(line)//2])
        secondHalf = set(line[len(line)//2:])

        for x in secondHalf:
            if x in firstHalf:
                # capital letter 
                if ord(x) < 91:
                    priorities += ord(x) - 38
                else:
                    priorities += ord(x) - 96
                exit

print(priorities)