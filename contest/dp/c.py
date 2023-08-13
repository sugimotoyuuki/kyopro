n = int(input())

dp = [[-1] * 3 for _ in range(n)]

a, b, c = map(int, input().split())
dp[0][0] = a
dp[0][1] = b
dp[0][2] = c
for i in range(1, n):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a, dp[i][0])
    dp[i][1] = max(dp[i - 1][0] + b, dp[i - 1][2] + b, dp[i][1])
    dp[i][2] = max(dp[i - 1][0] + c, dp[i - 1][1] + c, dp[i][2])

print(max(dp[-1]))
