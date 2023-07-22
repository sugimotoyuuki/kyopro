from collections import deque

n1, n2, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

G = [[] for _ in range(n1 + n2)]
for a, b in ab:
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


def bfs(st):
    dist = [-1 for _ in range(n1 + n2)]
    queue = deque([st])
    dist[st] = 0
    while queue:
        pos = queue.popleft()
        for to in G[pos]:
            if dist[to] == -1:
                dist[to] = dist[pos] + 1
                queue.append(to)
    return max(dist)


dist1 = bfs(0)
dist2 = bfs(n1 + n2 - 1)
print(dist1 + dist2 + 1)
