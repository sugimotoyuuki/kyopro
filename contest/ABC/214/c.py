n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

g = [list() for _ in range(n)]
for i in range(n):
    g[i].append((i + 1, s[i]))
    g[i + 1].append((i, s[i]))
