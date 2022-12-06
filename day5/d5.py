# AoC 2022 day 5
import re

# file = "example.txt"
file = "input.txt"
with open(file) as f:
    lines = f.read().splitlines()
print(lines)

if file == "example.txt":
    stacks = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

    print(stacks)

elif file == "input.txt":
    stacks = {
        1: ["F", "H", "B", "V", "R", "Q", "D", "P"],
        2: ["L", "D", "Z", "Q", "W", "V"],
        3: ["H", "L", "Z", "Q", "G", "R", "P", "C"],
        4: ["R", "D", "H", "F", "J", "V", "B"],
        5: ["Z", "W", "L", "C"],
        6: ["J", "R", "P", "N", "T", "G", "V", "M"],
        7: ["J", "R", "L", "V", "M", "B", "S"],
        8: ["D", "P", "J"],
        9: ["D", "C", "N", "W", "V"],
    }


instructions = [l for l in lines if "move" in l]
print(instructions)

for instruct in instructions:
    numbers = re.findall("\d+", instruct)
    number_to_move = int(numbers[0])
    origin_stack = int(numbers[1])
    destination_stack = int(numbers[2])
    for i in range(1, number_to_move + 1):
        stacks[destination_stack].append(stacks[origin_stack].pop())

answer1 = ""
for k, v in stacks.items():
    answer1 += v[-1]

print(answer1)
