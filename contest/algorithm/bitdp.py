n = int(input())
d = [[0] * 16 for _ in range(16)]
for i in range(n - 1):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp, i + 1):
        d[i][j] = t

dp = [0] * (1 << n)

for bit in range((1 << n) - 1):
    m = 0
    # bitに含まれない最小の端点をmとする
    for i in range(n):
        if not bit & (1 << i):
            m = i
            break
    # mに対してすべての点に対して全探索する
    for i in range(n):
        if not bit & (1 << i):
            nb = bit | (1 << m) | (1 << i)
            dp[nb] = max(dp[nb], dp[bit] + d[m][i])

print(dp[-1])
