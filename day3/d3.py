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


########################################
# part 2
start = 0
end = len(lines)
step = 3
groups = []
for i in range(start, end, step):
    x = i
    groups.append(lines[x : x + step])
print(groups)

part2_score = 0
for s in groups:
    a = list(set.intersection(*[set(e) for e in s]))[0]
    # print(a)
    part2_score += scores[a]
print(f"Part 2 Answer: {part2_score}")
