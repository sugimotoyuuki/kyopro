n, m = map(int, input().split())
s = [input() for _ in range(n)]


def check(i, j):
    for addi in range(3):
        for addj in range(3):
            if i + addi > n - 1 or j + addj > m - 1:
                return False
            if s[i + addi][j + addj] == ".":
                return False
    return True


ans = []
for i in range(n):
    for j in range(m):
        b = True
        if check(i, j) and check(i + 6, j + 6):
            tmp1, tmp2, tmp3, tmp4 = i + 3, j + 3, i + 5, j + 5
            for k in range(4):
                if (
                    s[tmp1 - k][tmp2] == "#"
                    or s[tmp1][tmp2 - k] == "#"
                    or s[tmp3 + k][tmp4] == "#"
                    or s[tmp3][tmp4 + k] == "#"
                ):
                    b = False
            if b:
                ans.append((i + 1, j + 1))

if ans:
    for i in ans:
        print(*i)
else:
    exit()
