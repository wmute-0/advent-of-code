with open("./resources/day1.txt", "r") as infile:
    data = infile.readlines()
    vals = [int(x) for x in data]
    seen = set()
    x = 0
    pos = 0
    # part 1
    print(sum(vals))
    # part 2
    while x not in seen:
        seen.add(x)
        x += vals[pos]
        pos = (pos + 1) % len(vals)
    print(x)