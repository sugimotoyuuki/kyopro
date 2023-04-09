# input
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
s.append([0, 0])
s.sort(key=lambda x: x[0], reverse=True)
s.sort(key=lambda x: x[1])

dp = [[-1] * 1449 for _ in range(n + 1)]

dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(1441):
        if s[i][0] > j or j > s[i][1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - s[i][0]] + 1)

ans = 0
for j in range(1441):
    ans = max(ans, dp[n][j])

print(ans)
