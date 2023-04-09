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
C = [list(input()) for _ in range(N)]

# グラフを構築
size = N + 24
S = size
T = size + 1
g = FordFulkerson(T + 1)

for i in range(size):
    if i < N:
        g.add_edge(S, i, 10)  # 10まで流せるようにする
    else:
        g.add_edge(i, T, M)  # M人以上

for i in range(N):
    for j, c in enumerate(C[i]):
        if c == "1":
            g.add_edge(i, j + N, 1)

print("Yes" if g.max_flow(S, T) == M * 24 else "No")
