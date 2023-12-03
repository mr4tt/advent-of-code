from collections import defaultdict

def gameFinder(file):
    sum = 0

    red = 12
    green = 13
    blue = 14

    with open(file, "r") as input:
        for line in input:
            split = line.split(":")
            games = split[1].split(";")
            
            marbles = defaultdict(int)
            for round in games:
                colors = round.split(",")

                for color in colors:
                    color = color.strip().split(" ")
                    marbleCount = int(color[0])
                    marbleColor = color[1]
                    
                    if marbleCount > marbles[marbleColor]:
                        marbles[marbleColor] = marbleCount

            power = 1
            for count in marbles.values():
                power *= count

            sum += power
    return sum

file = "day2_input.txt"
print("ans: ", gameFinder(file))