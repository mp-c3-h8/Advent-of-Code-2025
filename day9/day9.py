from itertools import combinations
from shapely import Polygon, prepare, box
from shapely.plotting import plot_polygon
import matplotlib.pyplot as plt


def get_area(c1, c2) -> int:
    return (abs(c1[0]-c2[0]) + 1) * (abs(c1[1]-c2[1]) + 1)


with open('input.txt', 'r') as f:
    coords = [tuple(map(int, line.split(","))) for line in f.readlines()]

polygon = Polygon(coords)
prepare(polygon)
plot_polygon(polygon)

sorted_pairs = sorted(combinations(coords, 2), key=lambda cc: get_area(cc[0], cc[1]), reverse=True)
print("Part 1:", get_area(*sorted_pairs[0]))

for c1, c2 in sorted_pairs:
    rect = box(c1[0], c1[1], c2[0], c2[1])
    if polygon.contains(rect):
        print("Part 2:", get_area(c1, c2))
        print("Rectangle:", c1, c2)
        plot_polygon(rect, color='orange')
        break

plt.show()
