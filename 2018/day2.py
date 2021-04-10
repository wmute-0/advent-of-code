from collections import Counter


with open("./resources/day2.txt", "r") as infile:
    data = infile.read().splitlines()
    twos = 0
    threes = 0
    # part 1 
    for line in data:
        c = Counter(line).values()
        twos += 2 in c
        threes += 3 in c
    print(twos * threes)
    # part 2
    for w1 in data:
        for w2 in data:
            diff = [a != b for (a, b) in zip(w1, w2)]
            if sum(diff) == 1:
                print(w1, w2)