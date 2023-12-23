from collections import defaultdict
import copy

def lowestLoc(file):
    def findMap(dictionary, mappings):
        new_mappings = []
        for start, end in mappings:
            saved = []
            for ranges in dictionary:
                ranges = ranges.split(" ")
                # print("ranges: ", ranges)
                ranges = [int(i) for i in ranges]
                r = range(ranges[1], ranges[1] + ranges[2])
                diff = ranges[0] - ranges[1] # -170
                if start in r and end in r:
                    new_mappings.append((start + diff, end + diff))
                    print("both")
                    saved.append((start, end))
                elif start in r and end not in r:
                    new_mappings.append((start + diff, ranges[0] + ranges[2]))
                    print("start, not end")
                    saved.append((start, ranges[1] + ranges[2]))
                elif start not in r and end in r:
                    new_mappings.append((ranges[0], end + diff))
                    print("end, not start")
                    saved.append((ranges[1], end))
                print("!!!:", new_mappings)

            saved.sort(key = lambda x: x[0])
            # print("saved: ", saved)
            newList = copy.deepcopy(saved)
            for i in range(len(saved) - 1):
                if saved[i + 1][0] - saved[i][1] == 0:
                    newList.append((saved[i][0], saved[i + 1][1]))
                    newList.remove(saved[i])
                    newList.remove(saved[i + 1])

            # print("newlist", newList)
            for savedOne, savedTwo in newList:
                print("start: ", start, "end: ", end)
                print("saved1", savedOne, "Saved2", savedTwo)
                if start == savedOne and end == savedTwo:
                    print("ED IS A BIG CLOWN")
                    break
                if start == savedOne and end != savedTwo:
                    new_mappings.append((savedTwo, end))
                    print("BACAW")
                elif start != savedOne and end == savedTwo:
                    new_mappings.append((start, savedTwo))
                    print(start, savedTwo)
                    print("BACAWTWO")
            if not saved:
                new_mappings.append((start, end))
                print("NOT SAVED")
        return new_mappings

    with open(file, "r") as input:
        maps = input.read().split("\n\n")

    arr = []
    for types in maps:
        arr.append(types.split(": ") if ": " in types else types.split(":\n"))

    seedList = arr[0][1].split(" ")
    seedList = [int(i) for i in seedList]
    
    mappings = []
    for x in range(0, len(seedList), 2):
        mappings.append((seedList[x], seedList[x] + seedList[x + 1]))
    print(mappings)
    printlist = ["seeds", "seed to soil", "soil to fert", "fert to water", "water to light", "light to temp", "temp to humid", "humid to loc"]
    for i in range(1, len(arr)):
        print("==============================================================")
        coolmap = arr[i][1].split("\n")
        # print("seeds:", mappings)
        # print(printlist[i], i, coolmap)
        mappings = findMap(coolmap, mappings)
        print("==============================================================")
    
    sorted_list = sorted(mappings, key=lambda x: x[0])
    print(sorted_list)
    print("yes duplicates") if len(sorted_list) > len(set(sorted_list)) else print("no duplicates")
    #print(findMap(arr[1][1].split("\n"), mappings))
    return min(mappings, key = lambda t: t[0])

file = "day5_inputTest.txt"
print("ans: ", lowestLoc(file))