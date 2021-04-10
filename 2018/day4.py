import re
from collections import Counter


with open("./resources/day4.txt", "r") as infile:
    data = infile.read().splitlines()
    guards = {}
    freqs = {}
    active = None
    start = 0

    for line in data:
        nums = [int(x) for x in re.findall("\d+", line)]
        x = nums[-1]
        if 'Guard' in line:
            active = x
        if 'asleep' in line:
            start = x 
        if 'wakes' in line:
            n = list(range(start, x))
            guards.setdefault(active, []).extend(n)


    sleepiest_guard = max(guards, key=lambda x: len(guards[x]))
    cnt = Counter(guards[sleepiest_guard])
    sleepiest_minute = cnt.most_common()[0][0]
    # part 1
    print(sleepiest_guard * sleepiest_minute)

    # part 2 
    for k, v in guards.items():
        cnt = Counter(v)
        minute, x = cnt.most_common()[0]
        freqs[(k, minute)] = x

    guard, m = max(freqs, key=lambda k: freqs[k])
    print(guard * m)