from collections import deque


# どの都市も移動可能
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]


def bfs(st):
    dist = [-1 for _ in range(n)]
    queue = deque([st])
    dist[st] = 0
    while queue:
        pos = queue.popleft()
        for to in g[pos]:
            if dist[to] == -1:
                dist[to] = dist[pos] + 1
                queue.append(to)
    return dist


g = [[] for _ in range(n)]
for a, b in ab:
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

a = bfs(0)
b = bfs(a.index(max(a)))

print(max(b) + 1)
