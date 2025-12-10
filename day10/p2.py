import re
from numpy import column_stack
from scipy.optimize import linprog

data = open('input.txt').read().splitlines()

count = 0
for line in data:
    joltages = re.search(r"(?<=\{).*(?=\})", line)
    buttons = re.findall(r"\((.*?)\)", line)

    b = [int(jolt) for jolt in joltages.group().split(",")] if joltages else []
    c = [1]*len(buttons)
    A = []
    for button in buttons:
        column = [0] * len(b)
        for n in map(int, button.split(",")):
            column[n] = 1
        A.append(column)
    A = column_stack(A)

    res = linprog(c, A_eq=A, b_eq=b, integrality=1, options={'presolve': False})
    if res.success:
        count += int(res.fun)

print("Part 2:", count)
