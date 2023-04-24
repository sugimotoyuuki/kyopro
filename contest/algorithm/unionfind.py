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

    def root_list(self):  # 親のsetを取得
        return {self.root(i) for i in range(n)}

    def count_root_v(self):  # 各根に対する頂点の数を求める
        count_v = [0] * self.N
        for i in range(self.N):
            count_v[self.root(i)] += 1
        return count_v

    # 各根に対する辺の数を求める,
    # parは親要素を表すのに不十分だが先の要素は0に更新されていくため成り立つ
    # 可読性は下がるが計算量は抑えられる
    """def count_root_edge(self, edges):
        count_edge = [0] * self.N
        for u, v in edges:  # 入力として辺が与えられて、それぞれ1を引いている必要がある
            if UF.par[u] == -1:
                count_edge[u] += 1
            else:
                count_edge[UF.par[u]] += 1

        return count_edge"""

    def count_root_edge(self, edges):  # 各根に対する辺の数を求める
        count_edge = [0] * self.N
        for u, _ in edges:  # 入力として辺が与えられて、それぞれ1を引いている必要がある
            count_edge[self.root(u)] += 1
        return count_edge


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
