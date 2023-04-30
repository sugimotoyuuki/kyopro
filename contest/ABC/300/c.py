h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]


x = min(h, w)
ans = [0] * x
for i in range(h):
    for j in range(w):
        batu = 0
        if c[i][j] == "#":
            for k in range(1, x + 1):
                try:
                    if (
                        c[i - k][j - k] == "#"
                        and c[i + k][j + k] == "#"
                        and c[i - k][j + k] == "#"
                        and c[i + k][j - k] == "#"
                    ):
                        batu += 1
                    else:
                        break
                except IndexError:
                    break
            if batu != 0:
                ans[batu - 1] += 1


print(*ans)
