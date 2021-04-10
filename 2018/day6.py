from collections import defaultdict

def manhatten_dist (p1, p2):
    return abs(p1[0] - p2[0])  + abs(p1[1] - p2[1])

with open("./resources/day6.txt", "r") as infile:
    data = [s.split(", ") for s in infile.read().splitlines()]
    coords = [(int(y), int(x)) for (x, y) in data]
    counter = defaultdict(int)

    # determine corners
    min_x = min([p[0] for p in coords])
    max_x = max([p[0] for p in coords])
    min_y = min([p[1] for p in coords])
    max_y = max([p[1] for p in coords])

    candidates = [(x, y) for (x, y) in coords if min_x < x < max_x and min_y < y < max_y]
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            # skip if point in coords
            if (i, j) in coords:
                continue
            dists = [manhatten_dist(p, (i, j)) for p in coords]
            shortest = min(dists)
            # skip if more than one shortest path
            if dists.count(shortest) > 1:
                continue
            pos = dists.index(shortest)
            k = coords[pos]
            counter[k] += 1

    # remove infinites
    result = [(k, v) for (k, v) in counter.items() if k in candidates]
    print(max(result, key=lambda x: x[1]))