def winRace(file):
    with open(file, "r") as input:
        info = input.read().split("\n")

    times = info[0].split(" ")
    times = [x for x in times if x != ""]
    
    distance = info[1].split(" ")
    distance = [x for x in distance if x != ""]

    # find number of ways to win a race 
    def findWays(time, dist):
        counter = 0
        for pressTime in range(time):
            if pressTime * (time - pressTime) > dist:
                counter += 1
        return counter

    ans = 1

    # calculate ways to win a race for each race
    for i in range(1, len(times)):
        ans *= findWays(int(times[i]), int(distance[i]))

    return ans

file = "day6_input.txt"
print("ans: ", winRace(file))