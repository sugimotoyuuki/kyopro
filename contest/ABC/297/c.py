# input
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

count_t = 0
for i, row in enumerate(s):
    count_t = 0
    for j, el in enumerate(row):
        if el == "T":
            count_t += 1
        else:
            count_t = 0
        if count_t == 2:
            s[i][j - 1] = "P"
            s[i][j] = "C"
            count_t = 0

for row in s:
    print(*row, sep="")
