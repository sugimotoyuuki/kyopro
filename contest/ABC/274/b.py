from collections import defaultdict

h, w = map(int, input().split())
c = [input() for _ in range(h)]

d = defaultdict(int)
for i, row in enumerate(c):
    for j, el in enumerate(row):
        if el == "#":
            d[j] += 1

for i in range(w):
    if i != w - 1:
        print(d.get(i, 0), end=" ")
    else:
        print(d.get(i, 0))
