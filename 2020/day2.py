import util 
import re
from collections import Counter

data = util.read_text_lines("./resources/day2.txt")
valid_count = 0
valid_count_p2 = 0
# part 1
for entry in data:
    min_v, max_v = [int(x) for x in re.findall("\d+", entry)]
    tgt, *chars = re.findall("[a-z]", entry)
    cnt = Counter(chars)
    valid_count += min_v <= cnt[tgt] <= max_v

# part 2
for entry in data:
    indices = [int(x) - 1 for x in re.findall("\d+", entry)]
    tgt, *chars = re.findall("[a-z]", entry)
    xs = [chars[i] == tgt for i in indices]
    valid_count_p2 += sum(xs) == 1

print(valid_count)
print(valid_count_p2)
