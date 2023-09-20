# ループすると思いこんでいたがそのようなことはない
m = int(input())
s = [list(map(int, list(input()))) for _ in range(3)]

ans = float("inf")
for i in range(3 * m):
    for j in range(3 * m):
        for k in range(3 * m):
            if (
                i != j
                and i != k
                and j != k
                and s[0][i % m] == s[1][j % m] == s[2][k % m]
            ):
                ans = min(ans, max(i, j, k))
print(ans if ans < float("inf") else -1)
