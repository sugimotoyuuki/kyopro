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

    def count_root_v(self):  # 各根に対する頂点の数を求める
        count_v = [0] * self.N
        for i in range(self.N):
            count_v[self.root(i)] += 1
        return count_v

    def count_root_edge(self, edges):  # 各根に対する辺の数を求める
        count_edge = [0] * self.N
        for u, _ in edges:  # 入力として辺が与えられて、それぞれ1を引いている必要がある
            count_edge[self.root(u)] += 1
        return count_edge


h, w = map(int, input().split())
q = int(input())
UF = UnionFind(h * w)
maze = [[-1] * w for _ in range(h)]
idx = 0
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, r, c = q
        r -= 1
        c -= 1
        maze[r][c] = idx
        idx += 1
        for dx, dy in dxy:
            nx = r + dx
            ny = c + dy
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != -1:
                UF.unite(maze[r][c], maze[nx][ny])
    else:
        _, ra, ca, rb, cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if maze[ra][ca] == -1 or maze[rb][cb] == -1:
            print("No")
        elif UF.same(maze[ra][ca], maze[rb][cb]):
            print("Yes")
        else:
            print("No")
