from itertools import combinations
from math import prod, dist

type Box = tuple[int, int, int]
type Circuit = set[Box]

boxes: set[Box] = set()
sorted_pairs: list[tuple[Box, Box]] = []
circuits: list[Circuit] = []
lastx: tuple[int, int] = (0, 0)


def find_circuit_index(b: Box) -> int:
    return next(i for i, circuit in enumerate(circuits) if b in circuit)


with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y, z = map(int, line.split(","))
        boxes.add((x, y, z))

sorted_pairs = sorted(combinations(boxes, 2), key=lambda comb: dist(*comb))

for i, (b1, b2) in enumerate(sorted_pairs):

    if i == 1000:
        print("Part 1:", prod(sorted(map(len, circuits))[-3:]))

    if len(circuits) == 1 and not boxes:
        print("Part 2:", prod(lastx))
        break

    lastx = (b1[0], b2[0])
    b1_is_in_boxes = b1 in boxes
    b2_is_in_boxes = b2 in boxes

    if b1_is_in_boxes and b2_is_in_boxes:  # new disjoint 2-circuit
        boxes.difference_update({b1, b2})
        circuits.append({b1, b2})
        continue

    if b1_is_in_boxes or b2_is_in_boxes:  # a circuit grows by 1
        if b2_is_in_boxes:
            b1, b2 = b2, b1
        boxes.remove(b1)
        circuits[find_circuit_index(b2)].add(b1)
        continue

    # both boxes already belong to a circuit
    if (i1 := find_circuit_index(b1)) != (i2 := find_circuit_index(b2)):
        # different circuits -> merge
        circuits[i1].update(circuits.pop(i2))
