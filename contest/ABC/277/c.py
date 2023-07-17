from collections import defaultdict
import sys

sys.setrecursionlimit(300000)  # 上限値変えなあかん


# pypy3だとTLE
def dfs(pos, G, visited, ans):
    visited[pos] = True
    for i in G[pos]:  # posに1がなければ、空のリストをイテレートする
        if visited[i] is False:
            ans = dfs(i, G, visited, ans)
    ans = max(ans, pos)
    return ans


n = int(input())
g = defaultdict(list)
visited = defaultdict(lambda: False)

for _ in range(n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 1
visited[1] = True
ans = dfs(1, g, visited, ans)

print(ans)
