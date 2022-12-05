# AoC 2022 day 4
import string

file = "example.txt"
file = "input.txt"
with open(file) as f:
    lines = f.read().splitlines()
print(lines)


def findOverlap(str_pair):
    f, s = str_pair.split(",")
    f0, f1 = f.split("-")
    s0, s1 = s.split("-")

    r_f = set(range(int(f0), int(f1) + 1))
    r_s = set(range(int(s0), int(s1) + 1))

    if r_f.issubset(r_s):
        return True
    elif r_s.issubset(r_f):
        return True
    else:
        return False


print(f"part 1 answer: {sum([findOverlap(s) for s in lines])}")
