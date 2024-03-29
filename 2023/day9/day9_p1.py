def mapTravel(file):
    rows = []
    with open(file, "r") as input:
        info = input.read().split("\n")

        for n in info:
            curr_items = []
            numbers = n.split(" ")
            for number in numbers:
                curr_items.append(int(number))
            
            rows.append(curr_items)
    
    ans = 0
    for row in rows:
        temp = row # contains the current pyramid row 
        pyramid = [row] # contains full pyramid
        # while temp is not all zeros
        while not all(elem == 0 for elem in temp):
            
            num_list = [] # current list of differences 
            # loops through each element in a row and calculate the differences
            for index in range(1, len(temp)):
                num_list.append(temp[index] - temp[index - 1])

            temp = num_list
            pyramid.append(num_list)

        # once the full pyramid is found, calculate the differences of the last elements to get the sum
        last_ele = 0
        # start at len -2 to ignore the 0 row
        for n in range(len(pyramid) - 2, -1, -1):
            last_ele = pyramid[n][-1] + last_ele
        ans += last_ele

    return ans


file = "day9_input.txt"
print("ans: ", mapTravel(file))