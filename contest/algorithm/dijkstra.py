import heapq as hq

# input
N, M = map(int, input().split())

G = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])
    G[B].append([A, C])

q = list()
dist = [int(2e9)] * (N + 1)
conf = [False] * (N + 1)

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
            hq.heappush(q, [dist[nex], nex])

for i in range(1, len(dist)):
    if dist[i] == int(2e9):
        print(-1)
    else:
        print(dist[i])
