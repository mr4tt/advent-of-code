from collections import defaultdict
import sys

sys.setrecursionlimit(40000)

ans = 0 
correct = []
file = open("input.txt").read().split("\n\n")

rules = file[0].splitlines()
pages = file[1].splitlines()

ruleMap = defaultdict(list)
for rule in rules:
    before, after = rule.split("|")
    ruleMap[after].append(before)

def checkList(pageList, ruleMap):
    seen = set()

    # # check if the first number follows the rules  
    # if pageList[0] in ruleMap.keys():
    #     for i in range(1, len(pageList)):
    #         if i in ruleMap[pageList[0]]:
    #             return False, i

    # check if the first number follows the rules  
    if pageList[0] in ruleMap.keys():
        for i in ruleMap[pageList[0]]:
            if i in pageList[1:]:
                # this only works if we assume pageList has no duplicates  
                return False, pageList.index(i)

    # check if the rest of them follow the rules 
    for i in range(1, len(pageList)):
        currPage = pageList[i]
        prevPage = pageList[i - 1]
        seen.add(prevPage)
        if currPage in ruleMap.keys():
            for n in ruleMap[currPage]:
                if n not in seen and n in pageList:
                    # this only works if we assume pageList has no duplicates  
                    return False, pageList.index(n)
    return True, 0

def rearrange(pageList, index):
    # print("pre-rearrange,", pageList)
    # print(index)    

    if index == 0:
        print("ERROR")
        raise SystemExit
     
    item = pageList[index]
    pageList.pop(index)
    pageList.insert(0, item)

    return pageList

for page in pages:
    pageList = page.split(",")
    result, index = checkList(pageList, ruleMap)
    if not result:
        while not result:
            arrangement = rearrange(pageList, index)
            result, index = checkList(pageList, ruleMap)
        # print("arrangement:", arrangement)
        correct.append(arrangement)

print(correct)

for pageList in correct:
    ans += int(pageList[len(pageList) // 2])

print(ans)