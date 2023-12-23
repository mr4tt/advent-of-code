from collections import defaultdict

def lowestLoc(file):
    def findMap(dictionary, items):
        # for each seed, check each given range to see if seed is inside
        # return list of corresponding nums
        rangeList = []
        for seed in items:
            seedFlag = False
            for ranges in dictionary:
                ranges = ranges.split(" ")
                ranges = [int(i) for i in ranges]
                if seed in range(ranges[1], ranges[1] + ranges[2]):
                    rangeList.append(ranges[0] + (seed - ranges[1]))
                    seedFlag = True
            if not seedFlag:
                rangeList.append(seed)

        return rangeList

    with open(file, "r") as input:
        maps = input.read().split("\n\n")

    arr = []
    for types in maps:
        arr.append(types.split(": ") if ": " in types else types.split(":\n"))

    # start with initial seeds, convert to int
    seedList = arr[0][1].split(" ")
    seedList = [int(i) for i in seedList]

    # for each map given, find the next pairing for it 
    for i in range(1, len(arr)):
        coolmap = arr[i][1].split("\n")
        seedList = findMap(coolmap, seedList)
        
    return min(seedList)

file = "day5_input.txt"
print("ans: ", lowestLoc(file))