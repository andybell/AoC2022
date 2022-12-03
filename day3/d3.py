# AoC 2022 day 2
import string

# file = "example.txt"
file = "input.txt"
with open(file) as f:
    lines = f.read().splitlines()

print(lines)

repeats = []

for e in lines:
    l = int(len(e) / 2)
    common = list(set(e[0:l]).intersection(set(e[l:])))[0]
    repeats.append(common)

print(repeats)

# construct letter scores
letters = string.ascii_lowercase + string.ascii_uppercase
scores = dict()
for i, let in enumerate(letters):
    scores[let] = i + 1

# find scores
total = sum([scores[c] for c in repeats])
print(f"Answer for part 1: {total}")
