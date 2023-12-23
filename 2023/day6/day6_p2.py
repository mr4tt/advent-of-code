def winRace(file):
    with open(file, "r") as input:
        info = input.read().split("\n")

    times = info[0].split(" ")
    times = [x for x in times if x != ""]
    times = int("".join(times[1:]))
    
    distance = info[1].split(" ")
    distance = [x for x in distance if x != ""]
    distance = int("".join(distance[1:]))

    # brute forcing; the non brute force way to do it is find the midpt (as that's the highest distance) and
    # keep moving forward by 1 until you find something that doesn't beat the record distance, then return that * 2
    # (* 2 to accommodate for both sides of the numbers around midpt)
    counter = 0
    for pressTime in range(times):
        if pressTime * (times - pressTime) > distance:
            counter += 1
    return counter

file = "day6_input.txt"
print("ans: ", winRace(file))