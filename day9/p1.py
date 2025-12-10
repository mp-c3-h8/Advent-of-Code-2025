from itertools import combinations

with open('input.txt', 'r') as f:
    coords = [tuple(map(int, line.split(","))) for line in f.readlines()]

max_area = 0
for c1, c2 in combinations(coords, 2):
    area = (abs(c1[0]-c2[0]) + 1) * (abs(c1[1]-c2[1]) + 1)
    max_area = max(max_area, area)

print("Part 1:", max_area)
