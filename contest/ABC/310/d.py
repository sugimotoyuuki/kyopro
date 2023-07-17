n, t, m = map(int, input().split())

g = [[i for i in range(1, n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].remove(b)
    g[b].remove(a)

print(g[1:])
