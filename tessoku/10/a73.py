import heapq


def dijkstra(edges, n):
    dist = [float("inf")] * (n + 1)  # distは各頂点間の距離
    visited = [False] * (n + 1)  # 訪問したかどうか
    prev = [-1] * (n + 1)  # 最短距離を通ったときの前の点
    tree_num = [0] * (n + 1)  # 木の数
    hq = list()  # heapq
    dist[1] = 0
    heapq.heappush(hq, [0, 1])

    while hq:
        _, pos = heapq.heappop(hq)
        if visited[pos] is True:
            continue
        visited[pos] = True
        for nex, cost, tree in edges[pos]:
            if dist[nex] > dist[pos] + cost or (
                dist[nex] == dist[pos] + cost and tree_num[pos] + tree > tree_num[nex]
            ):
                dist[nex] = dist[pos] + cost
                tree_num[nex] = tree_num[pos] + tree
                prev[nex] = pos
                heapq.heappush(hq, [dist[nex], nex])

    return dist[-1], tree_num[-1]


# input
N, M = map(int, input().split())

edges = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, C, D = map(int, input().split())
    edges[A].append([B, C, D])
    edges[B].append([A, C, D])

ans1, ans2 = dijkstra(edges, N)
print(ans1, ans2)
