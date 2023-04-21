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

    def count_root_v(self):  # 各根に対する頂点の数を求める
        count_v = [0] * self.N
        for i, p in enumerate(self.par):
            if p != -1:
                count_v[p] += 1
            else:
                count_v[i] += 1
        return count_v

    def count_root_edge(self, edges):
        count_edge = [0] * self.N
        for u, v in edges:  # 入力として辺が与えられて、それぞれ1を引いている必要がある
            if UF.par[u] == -1:
                count_edge[u] += 1
            else:
                count_edge[UF.par[u]] += 1

        return count_edge


# input
n, m = map(int, input().split())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

UF = UnionFind(n)


for u, v in edges:
    UF.unite(u, v)

count_v = UF.count_root_v()
count_edge = UF.count_root_edge(edges)

ans = "Yes" if count_v == count_edge else "No"
print(ans)
