from collections import deque


n, d = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(n)]

k = deque([0])
ans = [False] * n
ans[0] = True
while k:
    for j in range(n):
        if j == k[0]:
            continue
        dist = ((xy[k[0]][0] - xy[j][0]) ** 2 + (xy[k[0]][1] - xy[j][1]) ** 2) ** 0.5
        if dist <= d:
            if ans[j] is False:
                k.append(j)
            ans[j] = True
    k.popleft()

for a in ans:
    if a:
        print("Yes")
    else:
        print("No")
