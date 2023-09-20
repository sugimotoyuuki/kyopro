import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

g = {i: set() for i in range(n + 1)}
for _ in range(m):
    a, b, x, y = map(int, input().split())
    g[a].add((b, x, y))
    g[b].add((a, -x, -y))


visited = [False] * (n + 1)
ans = [None] * (n + 1)
ans[1] = (0, 0)


def dfs(pos, x, y):
    for row in g[pos]:
        to, nx, ny = row
        if not ans[to]:
            ans[to] = (x + nx, y + ny)
            dfs(to, x + nx, y + ny)


dfs(1, 0, 0)

for a in ans[1:]:
    if a:
        print(*a)
    else:
        print("undecidable")
