
presents: list[list[str]] = []
regions: list[tuple[int, int, list[int]]] = []

*presents_data, regions_data = open('input.txt').read().split("\n\n")

presents = [list(p.split()[1:]) for p in presents_data]
presents_area = [sum(row.count('#') for row in present) for present in presents]

for line in regions_data.splitlines():
    size, counts = line.split(": ")
    ax, ay = map(int, size.split("x"))
    regions.append((ax, ay, [int(c) for c in counts.split(" ")]))

not_possible = 0
possible = 0
to_check = 0
for region in regions:
    ax, ay, counts = region
    area = ax * ay
    min_needed_area = sum(a*b for a, b in zip(presents_area, counts))
    n = (ax // 3) * (ay // 3)  # number of available 3x3 squares
    if area < min_needed_area:
        not_possible += 1
    elif n >= sum(counts):
        possible += 1
    else:
        # these would need proper checking
        to_check += 1
        pass

# size check is enough for this (troll) problem and input
print("Possible:", possible)
print("Impossible:", not_possible)
print("Left to check:", to_check)
