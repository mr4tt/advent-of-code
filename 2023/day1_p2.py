def decode(file):
    # given a set of strings and a letter, identify if there's a digit inside 
    def findDigit(letterSet, letter):
        digitsSet = set(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
        digits = {"one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"}
        intersect = letterSet.intersection(digitsSet)

        if letter.isdigit() or len(intersect) != 0:
            return True, letter if letter.isdigit() else digits[list(intersect)[0]]
        else:
            return False, None

    calibrate = 0
    with open(file, "r") as input:
        for line in input:
            p1 = 0
            p2 = len(line) -1
            p1digit = None
            p2digit = None
            for letter in line:
                p1Set = set([line[p1:p1+3], line[p1:p1+4], line[p1:p1+5]])
                p1flag = False
                if not p1flag:
                    p1flag, p1digit = findDigit(p1Set, line[p1])
                    if not p1flag:
                        p1 += 1
                    
                p2Set = set([line[p2-3:p2], line[p2-4:p2], line[p2-5:p2]])
                p2flag = False
                if not p2flag:
                    p2flag, p2digit = findDigit(p2Set, line[p2])
                    if not p2flag:
                        p2 -= 1
                if p1digit and p2digit:
                    break
            calibrate += int(p1digit + p2digit)
    return calibrate

file = "day1_input.txt"
print("ans: ", decode(file))