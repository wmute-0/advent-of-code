with open("./resources/day1.txt", "r") as infile:
    data = infile.readlines()
    numbers = [int(x) for x in data]
    # part 1
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == 2020:
                print(n1 * n2)
                break
    # part 2
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)
