from math import lcm

def mapTravel(file):
    maps = {}
    starting = {}
    with open(file, "r") as input:
        info = input.read().split("\n\n")
        directions = info[0]

        for n in info[1].split("\n"):
            values = n.split(" = ")

            nodes = values[1].replace("(", "").replace(")", "").replace(",", "").split(" ")
            maps[values[0]] = (nodes[0], nodes[1])
            if values[0].endswith("A"):
                starting[values[0]] = (nodes[0], nodes[1])

    totalCount = []

    for start in starting:
        flag = False
        counter = 0
        current = maps[start]
        while(True):
            
            for n in range(len(directions)):
                if directions[n] == "L":
                    nextLetter = current[0]
                else:
                    nextLetter = current[1]
                current = maps[nextLetter]

                counter += 1

                if nextLetter.endswith("Z"):
                    totalCount.append(counter)
                    flag = True
                    break
            if flag == True:
                break
    return lcm(*totalCount)
    

file = "day8_input.txt"
print("ans: ", mapTravel(file))