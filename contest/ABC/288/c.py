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
        if RootU == RootV:
            return
        if self.siz[RootU] >= self.siz[RootV]:
            RootU, RootV = RootV, RootU
        self.par[RootU] = RootV
        self.siz[RootV] += self.siz[RootU]

    def same(self, u: int, v: int) -> bool:  # 同じ根かどうか
        return self.root(u) == self.root(v)

    def root_list(self):  # 親のsetを取得
        return {self.root(i) for i in range(n)}

    def count_root_v(self):  # 各根に対する頂点の数を求める
        count_v = [0] * self.N
        for i in range(self.N):
            count_v[self.root(i)] += 1
        return count_v

    def count_root_edge(self, edges):  # 各根に対する辺の数を求める
        count_edge = [0] * self.N
        for u, _ in edges:  # 入力として辺が与えられて、それぞれ1を引いている必要がある
            count_edge[UF.root(u)] += 1
        return count_edge


n, m = map(int, input().split())
g = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

UF = UnionFind(n)
for u, v in g:
    UF.unite(u, v)

v_num = sum(UF.count_root_v())  # 頂点の数
root_num = len(UF.root_list())  # 根の数
edge_num = sum(UF.count_root_edge(g))  # 辺の数
ans = edge_num - (v_num - root_num)  # 辺の数を頂点数 - 根の数 にすれば木になる
print(ans)
