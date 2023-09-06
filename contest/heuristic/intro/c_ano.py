def f():
    u = v = 0
    last = [0] * 26
    for d in range(D):
        u += c[t[d] - 1] * (d + 1 - last[t[d] - 1]) - sumc
        v += s[d][t[d] - 1] + u
        last[t[d] - 1] = d + 1
    print(v)


D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]

sumc = sum(c)

for _ in range(int(input())):
    d, q = map(int, input().split())
    t[d - 1] = q
    f()
