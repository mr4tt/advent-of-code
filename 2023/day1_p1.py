def decode(file):
    calibrate = 0
    with open(file, "r") as input:
        for line in input:
            p1 = 0
            p2 = len(line) -1
            for letter in line:
                if not line[p1].isdigit():
                    p1 += 1
                if not line[p2].isdigit():
                    p2 -= 1
                if line[p2].isdigit() and line[p1].isdigit():
                    break
            calibrate += int(line[p1] + line[p2])
    return calibrate
            

file = "day1_input.txt"
print("ans: ", decode(file))