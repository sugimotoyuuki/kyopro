n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort()
geta = 0
day = [0]
pill = [0]
for a, b in ab:
    geta += b
    day.append(a)
    pill.append(-b)

for i in range(n + 1):
    if i == 0:
        pill[i] = geta
    else:
        pill[i] += pill[i - 1]
    if pill[i] <= k:
        print(day[i] + 1)
        exit()
