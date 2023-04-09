# TODO: 復習
INF = 1 << 61


# 構造体の定義
class Edge:
    def __init__(self, to: int, cap: int, rev: int):
        self.to = to
        self.cap = cap
        self.rev = rev


class FordFulkerson:
    def __init__(self, N):
        self.size = N
        self.g = [list() for _ in range(N)]

    def add_edge(self, a, b, c):
        g = self.g
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        g[a].append(e)
        g[b].append(rev)

    def dfs(self, pos, goal, F):
        if pos == goal:
            return F
        self.visited[pos] = True
        for e in self.g[pos]:
            if e.cap > 0 and self.visited[e.to] is False:
                flow = self.dfs(e.to, goal, min(F, e.cap))
                if flow:
                    e.cap -= flow
                    e.rev.cap += flow
                    return flow
        return 0

    def max_flow(self, s, t):
        total_flow = 0
        while True:
            self.visited = [False] * self.size
            F = self.dfs(s, t, INF)

            # フローを流せなくなったら操作終了
            if F == 0:
                break
            total_flow += F
        return total_flow


N, M = map(int, input().split())
P = list(map(int, input().split()))

# グラフを構築
S = N
T = N + 1
g = FordFulkerson(T + 1)
# 多分最小カットの値
offset = 0
for i in range(N):
    if P[i] >= 0:
        # S -> i: 特急駅にしない場合
        offset += P[i]
        g.add_edge(S, i, P[i])
    else:
        # i -> T: 特急駅にする場合
        g.add_edge(i, T, -P[i])

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    # a -> bの間を行ける
    g.add_edge(A, B, INF)

print(offset - g.max_flow(S, T))
