n = int(input())

inf = float("inf")
dp = [[-inf, -inf] for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    x, y = map(int, input().split())

    # 食べるとき
    if x == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + y, dp[i][1] + y)
    elif x == 1:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + y)

    # 食べないとき
    dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
    dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])

print(max(dp[n][0], dp[n][1]))
