n, x, y = map(int, input().split())
pt = [list(map(int, input().split())) for _ in range(n - 1)]
Q = int(input())

for _ in range(Q):
    q = int(input())
    dp = [0] * n
    dp[0] = q + x
    dp[n - 1] = float("inf")
    for i in range(n - 1):
        dp[i + 1] = dp[i] + pt[i][0] + pt[i][1] - 1 - ((dp[i] - 1) % pt[i][0])
    print(dp[-1] + y)
