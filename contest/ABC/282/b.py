n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

ans = 0
solved = 0
for i1 in range(n):
    for i2 in range(i1 + 1, n):
        solved = 0
        for j in range(m):
            if s[i1][j] == "o" or s[i2][j] == "o":
                solved += 1
        if solved == m:
            ans += 1

print(ans)
