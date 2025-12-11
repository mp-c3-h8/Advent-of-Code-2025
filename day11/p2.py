from collections import defaultdict
from functools import cache

conns: dict[str, list[str]] = {}

data = open('input.txt').read().splitlines()
conns = {line[:3]: list(line[5:].split()) for line in data}


@cache
def dfs(start: str, target: str):
    if start == target:
        return 1
    return sum(dfs(c, target) for c in conns.get(start, []))


dac_out = dfs("dac", "out")
fft_dac = dfs("fft", "dac")
svr_fft = dfs("svr", "fft")
fft_out = dfs("fft", "out")
dac_fft = dfs("dac", "fft")
svr_dac = dfs("svr", "dac")

print("Part 2:", (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out))
