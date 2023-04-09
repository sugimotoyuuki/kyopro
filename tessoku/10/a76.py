import bisect

MOD = 1000000007
# input
n, w, L, R = map(int, input().split())

x = list()
x.append(0)
for i in list(map(int, input().split())):
    x.append(i)
x.append(w)

dp = [0] * (n + 2)
sum = [0] * (n + 2)  # 連続しているのでdpの累積和をとる
dp[0], sum[0] = 1, 1
for i in range(1, n + 2):
    posL = bisect.bisect_left(x, x[i] - R)  # 連続しているとき1番最初にする
    posR = bisect.bisect_right(x, x[i] - L) - 1  # sumはx[i]があるところの一つ前

    # posL - 1なので >= 1 だし、累積和なので一つ引く
    dp[i] = (sum[posR] if posR >= 0 else 0) - (sum[posL - 1] if posL >= 1 else 0)
    dp[i] %= MOD

    sum[i] = sum[i - 1] + dp[i]
    sum[i] %= MOD

    # print(posL, posR)

print(dp[n + 1])
