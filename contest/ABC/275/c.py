pawn = []
for i in range(9):
    tmp = input()
    for j in range(9):
        if tmp[j] == "#":
            pawn.append((i, j))

n = len(pawn)
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = pawn[i]
        b = pawn[j]
        di = b[0] - a[0]
        dj = b[1] - a[1]
        c = (b[0] - dj, b[1] + di)
        d = (c[0] - di, c[1] - dj)
        if c in pawn and d in pawn:
            ans += 1

print(ans // 4)
