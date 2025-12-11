from collections import deque

conns: dict[str, list[str]] = {}

data = open('input.txt').read().splitlines()
conns = {line[:3]: list(line[5:].split()) for line in data}
q = deque(['you'])

count = 0
while q:
    curr = q.popleft()
    for c in conns[curr]:
        if c == "out":
            count += 1
        else:
            q.append(c)
            

print(count)
