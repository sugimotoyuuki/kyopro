h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
f = "snuke"
rf = "ekuns"


diag = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
tmp = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            for k, d in enumerate(diag):
                for m, letter in enumerate(f[1:], 1):
                    x = i + d[0] * m
                    y = j + d[1] * m
                    if x >= h or y >= w or x < 0 or y < 0:
                        break
                    if s[x][y] != letter:
                        tmp = []
                        break
                    else:
                        tmp.append(s[x][y])
                    if tmp == list(f[1:]):
                        ans_x, ans_y = i + 1, j + 1
                        for _ in range(5):
                            print(ans_x, ans_y)
                            ans_x += d[0]
                            ans_y += d[1]
                        exit()
