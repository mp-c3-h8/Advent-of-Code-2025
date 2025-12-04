
type Coords = tuple[int, int]  # (y,x)
papers: set[Coords] = set()
remove: set[Coords] = set()
to_check: set[Coords] = set()


def getNeighbors(c: Coords) -> list[Coords]:
    y, x = c
    return [(y+1, x+1), (y+1, x), (y+1, x-1), (y, x+1), (y, x-1), (y-1, x+1), (y-1, x), (y-1, x-1)]


data = open("input.txt").read().splitlines()
papers = {(y, x) for y, line in enumerate(data) for x, n in enumerate(list(line)) if n == "@"}

ans = len(papers)
to_check = papers

while to_check:
    remove = {c for c in to_check if sum(n in papers for n in getNeighbors(c)) < 4}
    papers.difference_update(remove)
    to_check = {n for c in remove for n in getNeighbors(c) if n in papers}

print("Part 2:", ans-len(papers))
