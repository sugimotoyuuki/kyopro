import heapq


def dijkstra(edges, n):
    # distは各頂点間の距離
    dist = [float("inf")] * (n + 1)
    dist[1] = 0
    # 訪問したかどうか
    visited = [False] * (n + 1)
    # heapq
    hq = list()
    heapq.heappush(hq, [0, 1])

    while hq:
        _, pos = heapq.heappop(hq)
        if visited[pos] is True:
            continue
        visited[pos] = True
        for nex, cost in edges[pos]:
            if dist[nex] > dist[pos] + cost:
                dist[nex] = dist[pos] + cost
                heapq.heappush(hq, [dist[nex], nex])

    return dist


# input
N, M = map(int, input().split())

edges = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])

ans = dijkstra(edges, N)

for i in range(1, len(ans)):
    if ans[i] == float("inf"):
        print(-1)
    else:
        print(ans[i])
