from math import prod

data = open("input.txt").read().splitlines()
numbers = [line.split() for line in data[:-1]]
ans = 0

for i, op in enumerate(data[-1].split()):
    if op.strip() == "*":
        ans += prod(int(row[i]) for row in numbers)
    else:
        ans += sum(int(row[i]) for row in numbers)

print(ans)
