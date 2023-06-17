from collections import defaultdict

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

a = defaultdict(set)
for i, row in enumerate(s):
    for j, el in enumerate(row):
        if el == "#":
            a[i].add(j)

k = 0
for i in a:
    for j in a[i]:
        k = max(k, len(a[i]))

for i in a:
    for j in a[i]:
        if len(a[i]) == k:
            set1 = a[i]
        else:
            set2 = a[i]
            b = i

a = set1 ^ set2
for i in a:
    print(b + 1, i + 1)
