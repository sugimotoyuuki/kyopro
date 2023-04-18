n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


def rotate(a):
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = a[i][j]

    return rotated


for _ in range(4):
    ans = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                ans = False
    if ans:
        print("Yes")
        exit()
    a = rotate(a)

print("No")
