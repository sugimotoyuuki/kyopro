from collections import deque


n, m = map(int, input().split())
g = [list(input().split()) for _ in range(m)]

sy, sx, gy, gx = 0, 0, 0, 0
for i, row in enumerate(g):
    for j, el in enumerate(row):
        if el == "s":
            g[i][j] = 0
            sy, sx = i, j
        elif el == "g":
            g[i][j] = -1
            gy, gx = i, j
        elif el == "0":
            g[i][j] = -1

q = deque()
q.append([sy, sx])
while q:
    y, x = q.popleft()

    for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        if 0 <= dy + y and dy + y < m and 0 <= dx + x and dx + x < n:
            if g[dy + y][dx + x] == -1:
                g[dy + y][dx + x] = g[y][x] + 1
                q.append([dy + y, dx + x])

if g[gy][gx] != -1:
    print(g[gy][gx])
else:
    print("Fail")
