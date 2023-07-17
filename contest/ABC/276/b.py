n, m = map(int, input().split())
d = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for v in d.values():
    v.sort()
    print(len(v), *v)
