file = open("input.txt").read().splitlines()

numbers = []
operators = ("+", "*")

for line in file:
    ans, nums = line.split(": ")
    nums = nums.split(" ")
    numbers.append([int(ans), [int(x) for x in nums]])

# get every possible combo of operators of length n
def mixer(operators, n):
    mixes = [[]]
    for _ in range(n):
        newMix = []
        for mix in mixes:
            for op in operators: newMix.append(mix + [op])
        mixes = newMix
    return mixes

def find(key, vals):
    options = mixer(operators, len(vals) - 1)

    # for each possible operator combination, calculate num1 [op] num2 
    for option in options:
        num1 = vals[0]
        for count, operator in enumerate(option):
            if num1 > key: break
            num2 = vals[count + 1]

            if operator == "+":   num1 += num2
            elif operator == "*": num1 *= num2
 
        if num1 == key: return True
    return False

ans = 0
for key, vals in numbers:
    if find(key, vals):
        ans += key

print(ans)