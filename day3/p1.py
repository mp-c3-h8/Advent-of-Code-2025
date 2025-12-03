
data = open("input.txt").read().splitlines()
ans = 0
length = len(data[0])


for line in data:
    bank = list(map(int, line))
    d1, d2 = bank[0], bank[1]

    for i in range(1, length):
        jolt = bank[i]

        if jolt > d1 and i+1 < length:
            d1 = jolt
            d2 = bank[i+1]
            continue

        if jolt > d2:
            d2 = jolt

    ans += d1*10+d2

print(ans)
