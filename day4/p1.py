
type Coords = tuple[int, int]  # (y,x)
papers: set[Coords] = set()


def getNeighbors(c: Coords) -> list[Coords]:
    y, x = c
    return [(y+1, x+1), (y+1, x), (y+1, x-1), (y, x+1), (y, x-1), (y-1, x+1), (y-1, x), (y-1, x-1)]


data = open("input.txt").read().splitlines()
papers = {(y, x) for y, line in enumerate(data) for x, n in enumerate(list(line)) if n == "@"}

ans = sum(sum((n in papers) for n in getNeighbors(c)) < 4 for c in papers)
print(ans)
