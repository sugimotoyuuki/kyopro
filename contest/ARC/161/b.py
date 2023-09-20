from itertools import combinations as comb
from bisect import bisect_right

t = int(input())

bins = []
for i, j, k in comb(range(60), 3):
    tmp = ["0"] * 60
    tmp[-i - 1] = "1"
    tmp[-j - 1] = "1"
    tmp[-k - 1] = "1"
    bins.append(int("".join(tmp), 2))
bins.sort()

for _ in range(t):
    n = int(input())
    if n < 7:
        print(-1)
        continue
    print(bins[bisect_right(bins, n) - 1])
