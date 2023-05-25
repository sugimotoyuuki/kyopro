n, m = map(int, input().split())
s = [input() for _ in range(n)]

g = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        count = 0
        for let1, let2 in zip(s[i], s[j]):
            if let1 != let2:
                count += 1
        if count == 1:
            g[i].append(j)
            g[j].append(i)


def dfs_hamilton(v, seen):
    end = True
    for i, s in enumerate(seen):
        if not s and i != v:
            end = False
    if end:
        exit(print("Yes"))
    seen[v] = True
    for u in g[v]:
        if seen[u]:
            continue
        dfs_hamilton(u, seen)
    seen[v] = False  # 通り終えた点は初期化


res = 0
for i in range(n):
    seen = [False] * n
    dfs_hamilton(i, seen)
print("No")
