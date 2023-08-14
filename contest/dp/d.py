n, lim = map(int, input().split())
dp = [[-1] * (lim + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    w, v = map(int, input().split())
    for j in range(lim + 1):
        if dp[i][j] != -1:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
            if j + w <= lim:
                dp[i + 1][j + w] = max(dp[i][j] + v, dp[i + 1][j + w])


print(max(dp[-1]))
