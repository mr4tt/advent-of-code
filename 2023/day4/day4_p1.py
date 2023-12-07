def scratchWinner(file):
    sum = 0

    with open(file, "r") as input:
        for line in input:
            split = line.split(":")
            sides = split[1].split("|")

            # list of numbers without extraneous spaces 
            currNums = [x for x in sides[0].strip().split(" ") if x != ""]
            winNums = [x for x in sides[1].strip().split(" ") if x != ""]
            
            points = 0
            for num in currNums:
                if num in winNums and points == 0:
                    points = 1
                elif num in winNums:
                    points *= 2
            sum += points
    return sum

file = "day4_input.txt"
print("ans: ", scratchWinner(file))