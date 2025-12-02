
data = open("input.txt").read().splitlines()
dial = 50
ans = 0

for line in data:
    rot, val = line[0], int(line[1:])
    if rot == "R":
        dial += val
    else:
        dial -= val
        
    div, dial = divmod(dial,100)
    ans += abs(div)

print(ans)
