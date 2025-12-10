import re
from itertools import combinations

data = open('input.txt').read().splitlines()


def calc_presses(buttons: list[int], target: int) -> int:
    for i in range(len(buttons)):
        for subset in combinations(buttons, i):
            start = 0
            for elem in subset:
                start ^= elem  # bitwise XOR
            if start == target:
                return i
    return 0


ans = 0
for line in data:
    diagram_match = re.search(r"(?<=\[).*(?=\])", line)
    diagram = [c == "#" for c in diagram_match.group()] if diagram_match else []

    # reversed bits to int
    target = sum(1 << i for i, c in enumerate(diagram) if c)

    buttons_match = re.findall(r"\((.*?)\)", line)
    buttons_as_ints = [sum(1 << n for n in map(int, button.split(","))) for button in buttons_match]

    ans += calc_presses(buttons_as_ints, target)

print("Part 1:", ans)
