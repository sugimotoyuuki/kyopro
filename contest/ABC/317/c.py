n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

visited = [False] * n


def dfs(v, length):
    visited[v] = True
    max_len = length
    for next_v, w in g[v]:
        if not visited[next_v]:
            max_len = max(max_len, dfs(next_v, length + w))
    visited[v] = False
    return max_len


max_path = 0
for i in range(n):
    max_path = max(max_path, dfs(i, 0))

print(max_path)
