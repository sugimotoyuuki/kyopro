n = int(input())

dp = [[float("inf")] * (10**5 + 1) for _ in range(n + 1)]
dp[0][0] = 0
total_z = 0
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    total_z += z
    w = 0
    if y > x:
        w = (x + y) // 2 + 1 - x
    for j in range(10**5 + 1):
        if j - z >= 0:
            dp[i][j] = min(dp[i - 1][j - z] + w, dp[i][j], dp[i - 1][j])
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

ans = float("inf")
# 過半数以上でなければならない
for j in range(total_z // 2 + 1, total_z + 1):
    ans = min(ans, dp[-1][j])

print(ans)
