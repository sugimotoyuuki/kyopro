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

edges = list()
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges.append((A, B))

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

detouch = [False] * M  # 削除予定の辺をboolで保持
for q in query:
    if q[0] == 1:
        q[1] -= 1
        detouch[q[1]] = True
    else:
        q[1] -= 1
        q[2] -= 1

UF = UnionFind(N)
# 削除する辺以外を結合
for i, e in enumerate(edges):
    if not detouch[i]:
        UF.unite(e[0], e[1])

ans = list()
for q in reversed(query):
    if q[0] == 1:
        A, B = edges[q[1]]
        UF.unite(A, B)
    elif q[0] == 2:
        if UF.same(q[1], q[2]):
            ans.append("Yes")
        else:
            ans.append("No")

for a in reversed(ans):
    print(a)
