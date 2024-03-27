def mapTravel(file):
    maps = {}
    with open(file, "r") as input:
        info = input.read().split("\n\n")
        directions = info[0]
        print(directions)
        print(info[1])
        for n in info[1].split("\n"):
            # AAA = (BBB, CCC)
            values = n.split(" = ")
            print(values)
            # AAA, (BBB, CCC)
            nodes = values[1].replace("(", "").replace(")", "").replace(",", "").split(" ")
            maps[values[0]] = (nodes[0], nodes[1])
    print(directions)
    print(maps)
    counter = 0
    current = maps["AAA"]

    while(True):
        for n in range(len(directions)):
            if directions[n] == "L":
                nextLetter = current[0]
            else:
                nextLetter = current[1]
            
            current = maps[nextLetter]

            counter += 1

            if nextLetter == "ZZZ":
                return counter



file = "day8_input.txt"
print("ans: ", mapTravel(file))