x, y, z = map(int, input().split())
s = input()
n = len(s)
dp = [[0, 0] for _ in range(n + 1)]
dp[0][1] = z
for i in range(n):
    if s[i] == "A":
        dp[i + 1][0] = min(dp[i][0] + y, dp[i][1] + z + y)
        dp[i + 1][1] = min(dp[i][0] + z + x, dp[i][1] + x)
    else:
        dp[i + 1][0] = min(dp[i][0] + x, dp[i][1] + z + x)
        dp[i + 1][1] = min(dp[i][0] + z + y, dp[i][1] + y)
print(min(dp[n][0], dp[n][1]))
