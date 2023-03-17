# input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 1~Nに対して隣接リスト表現
G = [list() for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

max_len = 0
for i in range(1, N + 1):
    if len(G[i]) > max_len:
        max_len = len(G[i])
        ans = i

print(ans)
