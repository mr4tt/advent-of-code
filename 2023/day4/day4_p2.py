def scratchWinner(file):
    cardCount = {}
    cardMatches = {}
    with open(file, "r") as input:
        for line in input:
            split = line.split(":")
            card = split[0].split(" ")
            sides = split[1].split("|")

            # list of numbers without extraneous spaces 
            currNums = [x for x in sides[0].strip().split(" ") if x != ""]
            winNums = [x for x in sides[1].strip().split(" ") if x != ""]
            
            # find number of matches a card has 
            match = 0
            for num in currNums:
                if num in winNums:
                    match += 1

            cardMatches[int(card[-1])] = match
            cardCount[int(card[-1])] = 1

    # for each card, add 1 to the card count of j cards below 
    # (do this i times for the number of cards we have)
    for key, matches in cardMatches.items():
        for i in range(cardCount[key]):
            for j in range(matches):
                cardCount[key + j + 1] += 1
    
    # count up your cards
    return sum(cardCount.values())

file = "day4_input.txt"
print("ans: ", scratchWinner(file))