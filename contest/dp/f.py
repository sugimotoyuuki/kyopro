import pprint as pp

s = input()
t = input()
n = int(len(s))
m = int(len(t))


dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

row, col = n, m
ans = []
while row > 0 and col > 0:
    if s[row - 1] == t[col - 1]:  # 一つ前のものが1引かれているという条件を使ってしまうと、すべて0で埋め尽くされているのでバグとなる
        ans.append(s[row - 1])
        row -= 1
        col -= 1
    elif dp[row][col] == dp[row - 1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col - 1]:
        col -= 1

pp.pprint(dp)
print("".join(ans[::-1]))
