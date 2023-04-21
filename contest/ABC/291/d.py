MOD = 998244353

n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]
for i in range(1, n):
    for pre in range(2):
        for nex in range(2):
            if cards[i - 1][pre] != cards[i][nex]:  # 前のカードのオモテウラが違うなら
                dp[i][nex] += dp[i - 1][pre]  # 次のdpに配っていく
    dp[i][0] %= MOD
    dp[i][1] %= MOD


print((dp[n - 1][1] + dp[n - 1][0]) % MOD)  # オモテウラの場合の数を足し合わせる
