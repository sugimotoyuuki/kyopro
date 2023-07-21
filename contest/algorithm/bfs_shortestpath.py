from collections import deque

# input
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

passed = set()
G = [[] for _ in range(h * w)]

"""for i in range(h):
    for j in range(w):
        g[w * i + j].append(w * i + j)"""

for i in range(h):
    for j in range(w):
        passed.add(a[i][j])
        if i < h - 1 and not a[i + 1][j] in passed:
            G[w * i + j].append(w * (i + 1) + j)
            G[w * (i + 1) + j].append(w * i + j)
        if j < w - 1 and not a[i][j + 1] in passed:
            G[w * i + j].append(w * i + j + 1)
            G[w * i + j + 1].append(w * i + j)

# BFS
# stackを使えばDFSになる
end = h * w - 1
path_list = []
dist = [-1 for _ in range(h * w)]
queue = deque([(0, [])])

dist[0] = 0
while queue:
    pos, path = queue.popleft()
    print(pos)
    if pos == end:
        path_list.append(path + [pos])
    else:
        for to in G[pos]:
            if dist[to] == -1:
                dist[to] = dist[pos] + 1
                queue.append((to, path + [pos]))

# print(*dist)
# print(path_list)
