import sys

sys.setrecursionlimit(120000)


path = list()


# pypy3だとTLE
def dfs(pos, G, visited):
    path.append(pos)
    if pos == N:
        print(*path)
        exit(0)
    else:
        visited[pos] = True
        for nex in G[pos]:
            if visited[nex] is False:
                dfs(nex, G, visited)
                path.pop()


# input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 1~Nに対して隣接リスト表現
G = [list() for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
dfs(1, G, visited)
