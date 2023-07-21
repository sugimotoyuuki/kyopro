h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
snuke = ["s", "n", "u", "k", "e"]
if s[0][0] != "s":
    print("No")
    exit()

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * w for _ in range(h)]
st = [(0, 0)]

# 迷路はbfsでは計算量が多くなる
while st:
    x, y = st.pop()
    visited[x][y] = True
    if x == h - 1 and y == w - 1:
        print("Yes")
        exit()
    for dx, dy in dir:
        next_x, next_y = x + dx, y + dy
        next_idx = (snuke.index(s[x][y]) + 1) % 5
        if 0 <= next_x < h and 0 <= next_y < w:
            if visited[next_x][next_y]:
                continue
            if s[next_x][next_y] == snuke[next_idx]:
                st.append((next_x, next_y))
print("No")
