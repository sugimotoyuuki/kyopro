import sys

sys.setrecursionlimit(120000)


# input
N, T = map(int, input().split())
T -= 1
# 隣接リスト表現
G = [list() for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)
rank = [0] * N
r = 0


def dfs(parent: int, i: int) -> int:
    for j in G[i]:
        # jが親のときスキップ
        if j == parent:
            continue
        r = dfs(i, j) + 1  # 1ループ目ではi=TをparentとしてG[T]を展開する
        if rank[i] < r:
            rank[i] = r
    return rank[i]


# 最初はparentを持たないので-1
dfs(-1, T)
print(*rank)
