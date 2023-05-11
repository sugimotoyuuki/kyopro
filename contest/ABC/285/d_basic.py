import sys

sys.setrecursionlimit(10**6)

n = int(input())

g = {}
seen = {}
for _ in range(n):
    u, v = input().split()
    g.setdefault(u, [])
    g.setdefault(v, [])
    g[u].append(v)
    g[v].append(u)
    seen[u] = False
    seen[v] = False


def f(par, cur):
    seen[cur] = True
    for chi in g[cur]:
        if par != chi:  # 互いに結んでいるので子供を辿ったときその親が要素である場合は見逃す
            if seen[chi]:
                exit(print("No"))
            f(cur, chi)


for k in seen.keys():
    if not seen[k]:
        f(-1, k)

print("Yes")
