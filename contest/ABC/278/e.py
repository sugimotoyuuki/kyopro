H, W, n, h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

min_x = [W + 1] * n
max_x = [0] * n
min_y = [H + 1] * n
max_y = [0] * n

for i, row in enumerate(a):
    for j, color in enumerate(row):
        color -= 1
        min_x[color] = min(min_x[color], j)
        max_x[color] = max(max_x[color], j)
        min_y[color] = min(min_y[color], i)
        max_y[color] = max(max_y[color], i)


for i in range(H - h + 1):
    for j in range(W - w + 1):
        x, y = i + h, j + w
        ans = n
        color = a[i][j]
        for k in range(n):
            if (
                min_x[k] >= j
                and max_x[k] <= j + w - 1
                and min_y[k] >= i
                and max_y[k] <= i + h - 1
            ):
                ans -= 1
        if j == W - w:
            print(ans)
        else:
            print(ans, end=" ")
