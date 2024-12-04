import re

ans = 0
with open("input.txt", "r+") as file1:
    # find all groups that match the pattern
    pattern = r"mul\([\d,]+\)"
    muls = re.findall(pattern, file1.read())
    for mul in muls:
        mul = mul.split(",")
        num1 = mul[0].split("(")[1]
        num2 = mul[1].split(")")[0]
        ans += int(num1) * int(num2)

print(ans)
    