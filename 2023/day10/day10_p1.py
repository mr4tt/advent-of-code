import sys


def maze(file):
    dictionary = {
        "|": ["N", "S"], 
        "-": ["E", "W"], 
        "L": ["N", "E"], 
        "F": ["S", "E"], 
        "J": ["N", "W"],
        "7": ["S", "W"],
        ".": []
    }

    # python moment lol
    sys.setrecursionlimit(13890) 

    # 2d array of pipes
    rows = []
    s_coords = []
    with open(file, "r") as input:
        pipes = input.read().split("\n")

        for i in range(len(pipes)):
            pipe_row = []
            for j in range(len(pipes[0])):
                if pipes[i][j] == "S":
                    s_coords = [i, j]
                pipe_row.append(pipes[i][j])
            rows.append(pipe_row)

    s_flag, n_flag, e_flag, w_flag = False, False, False, False

    # need to check opposite letter in dictionary bc the dictionary shows the direction you could go from that pipe 
    # shows which paths are legal from starting pt 
    north = rows[s_coords[0] - 1][s_coords[1]]
    if "S" in dictionary[north]:
        n_flag = True

    south = rows[s_coords[0] + 1][s_coords[1]]
    if "N" in dictionary[south]:
        s_flag = True

    west = rows[s_coords[0]][s_coords[1] - 1]
    if "E" in dictionary[west]:
        w_flag = True

    east = rows[s_coords[0]][s_coords[1] + 1]
    if "W" in dictionary[east]:
        e_flag = True

    # identify what kind of pipe S is 
    start = ""
    if s_flag and n_flag:
        start = "|"
    elif s_flag and e_flag:
        start = "F"
    elif s_flag and w_flag:
        start = "7"
    elif n_flag and e_flag:
        start = "L"
    elif n_flag and w_flag:
        start = "J"
    elif w_flag and e_flag:
        start = "-"

    rows[s_coords[0]][s_coords[1]] = start

    def dfs(x, y, visited, longest):
        # if we reach start point and we've already traveled, save longest
        if x == s_coords[0] and y == s_coords[1] and len(visited) > 0:
            if len(visited) > longest:
                longest = len(visited)
                return longest

        possible = dictionary[rows[x][y]]

        if "E" in possible:
            if (x, y + 1) not in visited:
                visited.append((x, y + 1))
                return dfs(x, y + 1, visited, longest)

        if "N" in possible:
            if (x - 1, y) not in visited:
                visited.append((x - 1, y))
                return dfs(x - 1, y, visited, longest)

        if "W" in possible:
            if (x, y - 1) not in visited:
                visited.append((x, y - 1))
                return dfs(x, y - 1, visited, longest)

        if "S" in possible:
            if (x + 1, y) not in visited:
                visited.append((x + 1, y))
                return dfs(x + 1, y, visited, longest)

    # divide by 2 to figure out the farthest point from start
    print(dfs(s_coords[0], s_coords[1], [], 0) / 2)


file = "day10_input.txt"
maze(file)

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
"""