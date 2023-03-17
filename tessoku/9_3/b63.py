from collections import deque

# input
R, C = map(int, input().split())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

# init maze
maze = [[-1] * (C + 1) for _ in range(R + 1)]
# input maze
for i in range(1, R + 1):
    for j, el in enumerate(list(input()), 1):
        maze[i][j] = el

maze[start[0]][start[1]] = 1
point = 2
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if i == end[0] and j == end[1]:
            continue
        if maze[i][j] == "#":
            maze[i][j] = -1
        elif maze[i][j] == ".":
            maze[i][j] = point
            point += 1
maze[end[0]][end[1]] = point

G = [list() for _ in range(point + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if maze[i][j] > 0:
            if i > 1 and maze[i - 1][j] > 0:
                G[maze[i][j]].append(maze[i - 1][j])
            if j > 1 and maze[i][j - 1] > 0:
                G[maze[i][j]].append(maze[i][j - 1])
            if i < R and maze[i + 1][j] > 0:
                G[maze[i][j]].append(maze[i + 1][j])
            if j < C and maze[i][j + 1] > 0:
                G[maze[i][j]].append(maze[i][j + 1])

q = deque()
dist = [-1 for _ in range(point + 1)]

q.append(1)
dist[1] = 0
while len(q):
    pos = q[0]
    q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)


print(dist[point])
