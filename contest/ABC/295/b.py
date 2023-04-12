# input
r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]

for r1 in range(r):
    for c1 in range(c):
        if b[r1][c1].isdigit():
            bomb = int(b[r1][c1])
            b[r1][c1] = "."
            for r2 in range(r):
                for c2 in range(c):
                    if abs(r1 - r2) + abs(c1 - c2) <= bomb and not b[r2][c2].isdigit():
                        b[r2][c2] = "."

for row in b:
    print(*row, sep="")
