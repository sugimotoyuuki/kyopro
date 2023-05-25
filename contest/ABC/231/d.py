import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = {i: [] for i in range(n)}  # 辞書じゃなくて配列でも実装可
deg = [0] * (n)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1 if deg[u] < 2 else exit(print("No"))
    deg[v] += 1 if deg[v] < 2 else exit(print("No"))
seen = [False] * n


def f(par, cur):
    seen[cur] = True
    for chi in g[cur]:
        if par != chi:  # 互いに結んでいるので子供を辿ったときその親が要素である場合は見逃す
            if seen[chi]:
                exit(print("No"))
            f(cur, chi)


for v in range(n):
    if not seen[v]:
        f(-1, v)

print("Yes")
