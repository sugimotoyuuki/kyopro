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
N, Q = map(int, input().split())
UF = UnionFind(N)

for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 1:
        UF.unite(u, v)
    elif t == 2:
        if UF.same(u, v):
            print("Yes")
        else:
            print("No")
