n = int(input())
a = [list(input()) for _ in range(n)]
ra = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                ra[i][j] = a[i + 1][j]
            else:
                ra[i][j] = a[i][j - 1]
        elif i == n - 1:
            if j == n - 1:
                ra[i][j] = a[i - 1][j]
            else:
                ra[i][j] = a[i][j + 1]
        else:
            if j == 0:
                ra[i][j] = a[i + 1][j]
            elif j == n - 1:
                ra[i][j] = a[i - 1][j]
            else:
                ra[i][j] = a[i][j]


for row in ra:
    print(*row, sep="")
