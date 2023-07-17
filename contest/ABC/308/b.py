n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))

ans = 0
for i, el in enumerate(c):
    if el in d:
        ans += p[d.index(el) + 1]
    else:
        ans += p[0]

print(ans)
