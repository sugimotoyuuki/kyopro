n, x = map(int, input().split())
coins = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (x + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i, coin in enumerate(coins, 1):
    for j in range(x + 1):
        for s in range(coin[1] + 1):
            if dp[i - 1][j] == 1 and j + coin[0] * s <= x:
                dp[i][j + coin[0] * s] = 1

print("Yes") if dp[n][x] else print("No")
