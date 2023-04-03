INF = 1 << 31


# 構造体の定義
class maxflow_edges:
    def __init__(self, to: int, cap: int, rev: int):
        self.to = to
        self.cap = cap
        self.rev = rev


def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F
    used[pos] = True
    for v in G[pos]:
        if v.cap > 0 and used[v.to] is False:
            # 各頂点のv.capの最小値を再帰的に求める
            # goalまでusedがfalseなら, Fがflowに帰ってくる
            flow = dfs(v.to, goal, min(F, v.cap), G, used)
            if flow:
                v.cap -= flow
                # to → v方向のcapを増やしている
                # revについては本を参照
                G[v.to][v.rev].cap += flow
                return flow
    return 0


def ford_fulkerson(N, s, t, edges):
    G = [list() for _ in range(N + 1)]
    for a, b, c in edges:
        G[a].append(maxflow_edges(b, c, len(G[b])))
        G[b].append(maxflow_edges(a, 0, len(G[a]) - 1))  # G[a]に追加されたあとなので-1

    total_flow = 0
    # F(flow)が0になるまでやる
    while True:
        used = [False] * (N + 1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break
    return total_flow


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

ans = ford_fulkerson(N, 1, N, edges)
print(ans)
