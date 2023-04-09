from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
XYZ = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]


def get_next(pos, idx):
    state = list()
    for i in range(N):
        state.append((pos >> i) % 2)

    X, Y, Z = XYZ[idx]
    state[X] = 1 - state[X]
    state[Y] = 1 - state[Y]
    state[Z] = 1 - state[Z]

    ret = 0
    # toを10進数で返す
    for i in range(N):
        if state[i]:
            ret += 1 << i

    return ret


G = [list() for _ in range((1 << N) + 1)]
for i in range(1 << N):
    for j in range(M):
        next_state = get_next(i, j)
        G[i].append(next_state)

start = 0
for i, a in enumerate(A):
    if a:
        start += 1 << i
end = (1 << N) - 1

# BFS
dist = [-1 for _ in range(1 << N)]
q = deque()

q.append(start)
dist[start] = 0
while len(q):
    pos = q[0]
    q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)

print(dist[end])
