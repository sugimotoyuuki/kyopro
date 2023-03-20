import heapq as hq

# input
N, M = map(int, input().split())

G = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])
    G[B].append([A, C])

q = list()
"""
dist: 各点における最短距離その点を通ったか
conf: その点を通ったか
prev: 最短距離を通ったときの前の点
"""
dist = [int(2e9)] * (N + 1)
conf = [False] * (N + 1)
prev = [-1 for _ in range(N + 1)]
mindist = list()

dist[1] = 0
hq.heappush(q, [0, 1])

while q:
    posdist, pos = hq.heappop(q)
    if conf[pos] is True:
        continue
    conf[pos] = True
    for nex, cost in G[pos]:
        if dist[nex] > dist[pos] + cost:
            dist[nex] = dist[pos] + cost
            prev[nex] = pos  # 直前の点を保存
            hq.heappush(q, [dist[nex], nex])

# ゴールから復元
path = [N]
while path[-1] != 1:
    path.append(prev[path[-1]])

path.reverse()
print(*path)
