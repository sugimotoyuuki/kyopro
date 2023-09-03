from collections import defaultdict

n = int(input())

g = defaultdict(int)
for i in range(n - 1):
    d = list(map(int, input().split()))
    for j, el in enumerate(d, i + 1):
        g[(i, j)] = el

ans = 0
for i in range(2 ** len(g)):
    tmp = 0
    s = set()
    for j in range(n):
        if i in s or j in s:
            continue
        if (i >> j) & 1:
            tmp += g[(i, j)]
    ans = max(ans, tmp)

print(ans)
