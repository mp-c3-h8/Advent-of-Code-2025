import bisect

lower: list[int] = []  # sorted
upper: list[int] = []  # sorted


def update_intervals(a: int, b: int) -> None:
    upper_a = bisect.bisect_left(upper, a)
    if upper_a == len(upper):  # (a,b) is disjoint to all others and rightmost
        lower.insert(upper_a, a)
        upper.insert(upper_a, b)
        return

    lower_b = bisect.bisect_right(lower, b)
    if lower_b == 0:  # (a,b) is disjoint to all others and leftmost
        lower.insert(lower_b, a)
        upper.insert(lower_b, b)
        return

    if upper_a == lower_b:  # (a,b) is disjoint to all others and inbetween
        lower.insert(upper_a, a)
        upper.insert(upper_a, b)
        return

    # overlapping
    # combine leftmost overlap and repeat
    # better: combine all overlaps at once
    new_a = min(lower[upper_a], a)
    new_b = max(upper[upper_a], b)
    lower.pop(upper_a)
    upper.pop(upper_a)
    update_intervals(new_a, new_b)


def print_intervals() -> None:
    for a, b in zip(lower, upper):
        print(a, "-", b)


data_ranges, data_ids = open("input.txt").read().split("\n\n")


# build disjoint intervals
for line in data_ranges.splitlines():
    a, b = map(int, line.split("-", 2))
    update_intervals(a, b)

# print_intervals()

p1 = 0
for item in map(int, data_ids.splitlines()):
    i = bisect.bisect_left(upper, item)
    if i != len(upper) and lower[i] <= item:
        p1 += 1

p2 = sum(b-a+1 for a, b in zip(lower, upper))

print("Part 1:", p1)
print("Part 2:", p2)
