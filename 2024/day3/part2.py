import re

ans = 0
with open("input.txt", "r+") as file1:
    todo = []
    pattern = r"mul\([\d,]+\)"

    # remove all pieces with dont() in front
    file = file1.read().split("do()")
    for piece in file:
        piece = piece.split("don't()")
        todo.append(piece[0])

    # find groups that match the pattern in a do()
    todo = "".join(todo)
    muls = re.findall(pattern, todo)
    for mul in muls:
        mul = mul.split(",")
        num1 = mul[0].split("(")[1]
        num2 = mul[1].split(")")[0]
        ans += int(num1) * int(num2)

print(ans)
    