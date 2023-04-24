import sys

sys.setrecursionlimit(120000)


# pypy3だとTLE
def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] is False:
            dfs(i, G, visited)


# input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 1~Nに対して隣接リスト表現
G = [list() for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
dfs(1, G, visited)

ans = True
for i in range(1, N + 1):
    if visited[i] is False:
        ans = False

if ans is True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
