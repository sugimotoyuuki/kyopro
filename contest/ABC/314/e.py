n, m = map(int, input().split())
rou = [list(map(int, input().split())) for _ in range(n)]
dp = [float("inf")] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    for r in rou:
        now = 0
        b = 0
        c, p, *s = r
        for el in s:
            if el:
                now += dp[max(0, i - el)]
            else:
                b += 1
        now /= p
        b /= p
        now += c
        now /= 1 - b
        dp[i] = min(dp[i], now)

print(dp[m])
