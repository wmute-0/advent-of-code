import re
from collections import defaultdict

with open("./resources/day3.txt", "r") as infile:
    data = infile.read().splitlines()
    grid = defaultdict(int)
    for line in data:
        _, x, y, w, h = [int(i) for i in re.findall("\d+", line)]
        for i in range(x, x + w):
            for j in range(y, y + h):
                grid[(i, j)] += 1
    # part 1
    p1_result = [v for v in grid.values() if v >= 2]
    print(len(p1_result))
    # part 2 
    for line in data:
        _, x, y, w, h = [int(i) for i in re.findall("\d+", line)]
        res = []
        for i in range(x, x + w):
            for j in range(y, y + h):
                res.append(grid[(i, j)] == 1)
        if all(p == 1 for p in res):
            print(line)