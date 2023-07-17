from collections import deque

h, w = map(int, input().split())
s = [list() for _ in range(h)]
idx = 0
for i in range(h):
    for el in input():
        idx += 1
        if el == "s":
            s[i].append(0)
        elif el == "n":
            s[i].append(1)
        elif el == "u":
            s[i].append(2)
        elif el == "k":
            s[i].append(3)
        elif el == "e":
            s[i].append(4)
        else:
            s[i].append(100)

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_num = 0
que = deque()
que.append((0, 0))
idx = 0
while que:
    x, y = que.popleft()
    if x == h - 1 and y == w - 1:
        print("Yes")
        exit()
    curr_num = s[x][y]
    for d in dir:
        next_x, next_y = x + d[0], y + d[1]
        if 0 <= next_x < h and 0 <= next_y < w:
            if s[next_x][next_y] == curr_num + 1 or (
                curr_num == 4 and s[next_x][next_y] == 0
            ):
                que.append((next_x, next_y))
print("No")
