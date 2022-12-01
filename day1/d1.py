# AoC 2022 day 1
input = "example.txt"
input = "input.txt"
with open(input) as f:
    lines = f.read().splitlines()
    
index = 0    
c = [[]]
for l in lines:
    if l == "":
        index+=1
        c.append([])
    else:
        c[index] = c[index] + [int(l)]
        
# sums
s = [sum(e) for e in c]

print(f"part 1 answer: {max(s)}")

# part 2
s_sorted = sorted(s, reverse=True)
print(f"part 2 answer: {sum(s_sorted[0:3])}")
