class UnionFind:
    def __init__(self, N: int) -> None:
        self.N = N
        self.par = [-1 for _ in range(N + 1)]
        self.siz = [1 for _ in range(N + 1)]

    def root(self, x: int) -> int:
        while True:
            if self.par[x] == -1:
                break
            x = self.par[x]  # xが-1でなければxに該当する親を代入する
        return x

    def unite(self, u: int, v: int) -> None:
        RootU = self.root(u)
        RootV = self.root(v)
        if RootU != RootV:
            if self.siz[RootU] < self.siz[RootV]:
                self.par[RootU] = RootV
                self.siz[RootV] += self.siz[RootU]
            else:
                self.par[RootV] = RootU
                self.siz[RootU] += self.siz[RootV]

    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)


# input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda x: x[2])  # 重みの小さい順にソートする
UF = UnionFind(N)

UF.unite(edges[0][0], edges[0][1])
ans = 0
for i, e in enumerate(edges):
    if i == 0:
        UF.unite(e[0], e[1])
        ans += e[2]
    else:
        if not UF.same(e[0], e[1]):
            UF.unite(e[0], e[1])
            ans += e[2]

print(ans)
