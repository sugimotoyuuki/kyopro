n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * n
dp[0] = 0

for i, el in enumerate(h):
    for j in range(1, k + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))

print(dp[-1])
