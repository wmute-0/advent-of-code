import util
import functools

data = util.read_text_lines("./resources/day3.txt")
x, y = (0, 0)
tree_count = 0
width = len(data[0])
height = len(data)
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

# part 1
while  x < height:
    tree_count += data[x][y % width] == "#"
    x += 1
    y += 3
print(tree_count)

# part 2
counts = []
for (i, j) in slopes:
    tree_count = 0
    (x, y) = (0, 0)
    while x < height:
        tree_count += data[x][y % width] == "#"
        x += i
        y += j
    counts.append(tree_count)

print(functools.reduce(lambda acc, x: acc * x, counts))
