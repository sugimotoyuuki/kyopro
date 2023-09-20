from sys import setrecursionlimit

setrecursionlimit(10**8)


n = int(input())
cp = [map(int, input().split()) for _ in range(n)]
g = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    c, *p = cp[i - 1]
    g[i] = p

path = []
visited = [False] * (n + 1)


# pypy3だとTLE
def dfs(pos):
    visited[pos] = True
    for i in g[pos]:
        if not visited[i]:
            dfs(i)
            path.append(i)


dfs(1)
print(*path)
