def validate(key, value):
    if key == "byr":
        return 1920 <= int(value) <= 2002
    if key == "iyr":
        return 2010 <= int(value) <= 2020
    if key == "eyr":
        return 2020 <= int(value) <= 2030
    if key == "hgt":
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        if value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
        return False
    if key == "hcl":
        if value[0] != "#":
            return False
        if len(value) != 7:
            return False
        return all(c in "0123456789abcdef" for c in value[1:])
    if key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        if len(value) != 9:
            return False
        return all(x in "0123456789" for x in value)


with open("./resources/day4.txt", "r") as infile:
    data = infile.read()
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    segments = data.split("\n\n")
    valid = 0
    valid_p2 = 0
    # part 1
    for sgm in segments:
        fields = dict([f.split(":") for f in sgm.split()])
        ks = fields.keys()
        valid += all(x in ks for x in required_fields)
        valid_p2 += all(validate(k, v) for (k, v) in fields.items())
    print(valid)
    print(valid_p2)