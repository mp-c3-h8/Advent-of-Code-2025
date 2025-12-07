
data = open("input.txt").read().splitlines()
row = [0 if c == "." else 1 for c in data[0]]
p1 = 0

for line in data[1:]:
    for i, c in enumerate(line):
        if c != "." and row[i]:  # hit a splitter with ray from above
            row[i-1] += row[i]  # can go left
            row[i+1] += row[i]  # or right
            row[i] = 0  # splitter blocks ray
            p1 += 1

print("Part 1:", p1)
print("Part 2:", sum(row))
