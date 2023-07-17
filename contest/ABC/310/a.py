n, p, q = map(int, input().split())
d = list(map(int, input().split()))
d.sort()
if p > d[0] + q:
    print(d[0] + q)
else:
    print(p)
