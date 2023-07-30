n, x, y = map(int, input().split())
a = list(map(int, input().split()))

width = 2 * 10**4 + 1
hor = list()
ver = list()
for i, a in enumerate(a):
    if i == 0:
        geta = a
        continue
    if i % 2 == 0:
        hor.append(a)
    else:
        ver.append(a)


def solve(a, doko, geta=0):
    m = len(a)
    dp = [[0] * width for _ in range(m + 1)]
    dp[0][10000 + geta] = 1
    for i in range(m):
        for j in range(width):
            if dp[i][j] == 1:
                if j + a[i] < width:
                    dp[i + 1][j + a[i]] = 1
                if 0 <= j - a[i]:
                    dp[i + 1][j - a[i]] = 1
                dp[i][j] = 0
    # return dp
    return dp[m][doko + 10000]


# ans = solve(hor, x, geta)
# print(ans[len(hor)][x + 10000])
if solve(hor, x, geta) and solve(ver, y):
    print("Yes")
else:
    print("No")
