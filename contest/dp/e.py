n, lim = map(int, input().split())
dp = [[float("inf")] * (10**5 + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    w, v = map(int, input().split())
    for j in range(10**5 + 1):
        if dp[i][j] != -1:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            if dp[i][j] + w <= lim:
                dp[i + 1][j + v] = min(dp[i][j] + w, dp[i + 1][j + v])

for j, el in enumerate(dp[-1]):
    if el != float("inf"):
        val = j

print(val)
