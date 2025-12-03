
def calc_joltage(bank: list[int], n: int) -> int:
    len_bank = len(bank)
    res_indices = list(range(0, n))  # init result with leftmost n batteries (indices)

    for i in range(1, len_bank):
        for (j, res_index) in enumerate(res_indices):
            if i <= res_index:
                break
            dist = i+n-j
            if bank[i] > bank[res_index] and dist-1 < len_bank:
                res_indices[j:] = list(range(i, dist))  # len(LHS) = n-j = len(RHS)
                break
    return sum(10**(n-j-1)*bank[res_index] for (j, res_index) in enumerate(res_indices))


data = open("input.txt").read().splitlines()
p1, p2 = 0, 0


for line in data:
    bank = list(map(int, line))
    p1 += calc_joltage(bank, 2)
    p2 += calc_joltage(bank, 12)

print("Part 1:", p1)
print("Part 2:", p2)
