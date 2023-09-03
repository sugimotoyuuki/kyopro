n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
area = [[False] * (101) for _ in range(101)]

for a, b, c, d in li:
    for i in range(a, b):
        for j in range(c, d):
            area[i][j] = True

ans = 0
for i in range(101):
    for j in range(101):
        if area[i][j]:
            ans += 1
print(ans)
