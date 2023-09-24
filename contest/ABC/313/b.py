n, m = map(int, input().split())

g = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

saikyo = []
for k, v in g.items():
    if v:
        continue
    saikyo.append(k)

if len(saikyo) == 1:
    print(saikyo[0])
else:
    print(-1)
