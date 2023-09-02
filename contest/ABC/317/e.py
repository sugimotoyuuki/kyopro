from collections import deque, defaultdict
from pprint import pprint

# 入力
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

# SとGの位置を求める
for i in range(h):
    left, right = False, False
    for j in range(w):
        if maze[i][j] == ".":
            if left:
                maze[i][j] = "#"
            if right:
                maze[i][j] = "#"
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "G":
            goal = (i, j)
        if maze[i][j] == ">":
            maze[i][j] = "#"
            right = True
        if maze[i][j] == "<":
            maze[i][j] = "#"
            right = False
            left = True
pprint(maze)

# # 移動方向（上、右、下、左）
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# # 各マスへの最短距離を保存するテーブル
# dist = [[-1] * w for _ in range(h)]
# dist[start[0]][start[1]] = 0

# # BFSのキュー
# queue = deque([start])

# d = {r: []}
# while queue:
#     x, y = queue.popleft()

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]

#         # マップの範囲内か、障害物や既に訪れたマスでないかを確認
#         if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "#" and dist[nx][ny] == -1:
#             queue.append((nx, ny))
#             dist[nx][ny] = dist[x][y] + 1

# print(dist[goal[0]][goal[1]])
