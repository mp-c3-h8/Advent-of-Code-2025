import re

data = open("input.txt").read().split(",")
ans = 0

for line in data:
    (start, end) = line.split("-", 2)

    for i in range(int(start), int(end)+1):
        s = str(i)
        l = len(s)

        for j in range(1, l//2 + 1):

            if l % j != 0:
                continue

            check = s[:j]
            if s.count(check) == l//j:
                ans += i
                break

print(ans)
