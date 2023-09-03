n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
# while True:

ans = 0
while f:
    tmp = 0
    if len(f) >= d:
        for _ in range(d):
            tmp += f.pop()
        if tmp >= p:
            ans += p
        else:
            ans += tmp
    else:
        tmp = sum(f)
        f = []
        if tmp > p:
            ans += p
        else:
            ans += tmp

print(ans)
