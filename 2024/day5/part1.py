from collections import defaultdict

ans = 0 
file = open("input.txt").read().split("\n\n")

rules = file[0].splitlines()
pages = file[1].splitlines()

ruleMap = defaultdict(list)
for rule in rules:
    before, after = rule.split("|")
    ruleMap[after].append(before)

def checkList(pageList, ruleMap):
    seen = set()

    # check if the first number follows the rules  
    if pageList[0] in ruleMap.keys():
        for i in ruleMap[pageList[0]]:
            if i in pageList[1:]:
                return False

    # check if the rest of them follow the rules 
    for i in range(1, len(pageList)):
        currPage = pageList[i]
        prevPage = pageList[i - 1]
        seen.add(prevPage)
        if currPage in ruleMap.keys():
            for n in ruleMap[currPage]:
                if n not in seen and n in pageList:
                    return False
    return True

for page in pages:
    pageList = page.split(",")
    if checkList(pageList, ruleMap):
        ans += int(pageList[len(pageList) // 2])

print(ans)