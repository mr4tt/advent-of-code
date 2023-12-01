from itertools import islice

input = "day3\\input3.txt"

priorities = 0

set1, set2, set3 = set()
input = open(input).read().split("\n")

with open(input, "r") as file:
    for line in file:
        set1 = set()
        # letters = dict()

        # for char in threelines:
        #     if char in letters:
        #         letters[char] += 1
        #         if letters[char] == 3:
        #             if ord(char) < 91:
        #                 priorities += ord(char) - 38
        #             else:
        #                 priorities += ord(char) - 96
        #             continue
        #     else:
        #         letters[char] = 1

print(priorities)