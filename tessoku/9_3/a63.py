import sys
from collections import deque


sys.setrecursionlimit(120000)


# input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
# 1~Nに対して隣接リスト表現
G = [list() for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

dist = [-1 for _ in range(N + 1)]
q = deque()

q.append(1)
dist[1] = 0
while len(q):
    pos = q[0]
    q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)

print(*dist[1:])
