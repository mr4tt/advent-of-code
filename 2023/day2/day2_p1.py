from collections import defaultdict

def gameFinder(file):
    sum = 0

    red = 12
    green = 13
    blue = 14

    with open(file, "r") as input:
        for line in input:
            split = line.split(":")
            id = split[0].split(" ")[1]
            games = split[1].split(";")
            
            marbles = defaultdict(int)
            for round in games:
                colors = round.split(",")

                for color in colors:
                    color = color.strip().split(" ")
                    marbleCount = int(color[0])
                    marbleColor = color[1]
                    
                    marbles[marbleColor] = 0 if marbleCount < marbles[marbleColor] else marbleCount - marbles[marbleColor]

            if marbles["green"] > green or marbles["red"] > red or marbles["blue"] > blue:
                continue
            sum += int(id)
    return sum

file = "day2_input.txt"
print("ans: ", gameFinder(file))