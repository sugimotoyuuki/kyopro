# input
n = int(input())
p = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

# x, yを定義
x = [0] * n
y = [0] * n
for i, row in enumerate(p):
    for j, el in enumerate(row):
        if el >= 0:
            x[i] = el
            y[j] = el

# 転倒数を求める
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if x[i] > x[j]:
            count += 1
        if y[i] > y[j]:
            count += 1

print(count)
