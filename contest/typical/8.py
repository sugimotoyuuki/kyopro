n = int(input())
s = input()
atc = "atcoder"
MOD = 10**9 + 7

dp = [[0] * 8 for _ in range(n + 1)]
dp[0][0] = 1


for i in range(n):
    for j in range(8):
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
        if j < 7 and s[i] == atc[j]:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD

print(dp[-1][-1])
