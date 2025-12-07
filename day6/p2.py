from math import prod

data = open("input.txt").read().splitlines()
chars = [line[::-1] for line in data]  # reverse
ans = 0

vals = []
for column in zip(*chars):
    val = "".join(column[:-1]).strip()
    if len(val):
        vals.append(int(val))
    if column[-1] == "+":
        ans += sum(vals)
        vals = []
    elif column[-1] == "*":
        ans += prod(vals)
        vals = []

print(ans)
