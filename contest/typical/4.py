h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

row_sum = [0] * h
col_sum = [0] * w
for i in range(h):
    for j in range(w):
        row_sum[i] += a[i][j]
        col_sum[j] += a[i][j]

ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = row_sum[i] + col_sum[j] - a[i][j]

for row in ans:
    print(*row)
