class UnionFind:
    def __init__(self, N: int) -> None:
        self.N = N
        self.par = [-1 for _ in range(N)]
        self.siz = [1 for _ in range(N)]

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

    def same(self, u: int, v: int) -> bool:  # 同じ根かどうか
        return self.root(u) == self.root(v)

    def par_list(self):  # 親のリストを取得
        return [i for i, j in enumerate(self.par) if j < 0]


# input
n, m = map(int, input().split())

UF = UnionFind(n)
x = 0
for _ in range(m):
    a, _, c, _ = input().split()
    u, v = int(a) - 1, int(c) - 1
    if UF.same(u, v):
        x += 1
    UF.unite(u, v)

par_num = len(UF.par_list())
print(x, par_num - x)
