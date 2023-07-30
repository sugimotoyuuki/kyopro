import sys

sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
s = [input() for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
stopped = [[False] * m for _ in range(n)]
passed = [[False] * m for _ in range(n)]


def dfs(x, y):
    stopped[x][y] = True
    for i in range(4):
        nx, ny = x, y
        while s[nx + dx[i]][ny + dy[i]] == ".":
            nx += dx[i]
            ny += dy[i]
            passed[nx][ny] = True
        if stopped[nx][ny]:  # すでに止まっていたらcontinue
            continue
        dfs(nx, ny)


passed[1][1] = True  # スタート地点は通過済み
dfs(1, 1)
print(sum(sum(p) for p in passed))
