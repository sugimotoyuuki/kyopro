h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
for row in s:
    for el in row:
        if el == "#":
            ans += 1

print(ans)
