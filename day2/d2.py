# AoC 2022 day 2
# file = "example.txt"
file = "input.txt"
with open(file) as f:
    lines = f.read().splitlines()

print(lines)
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
rps_scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

scores = [rps_scores[t] for t in lines]
print(f"part 1: {sum(scores)}")


########################################
## shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)

rps_op_scores = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

op_scores = [rps_op_scores[t] for t in lines]
print(f"part 2: {sum(op_scores)}")
