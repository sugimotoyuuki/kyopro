n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

search = set(c)
d = {i: [0, 0] for i in search}

for idx, (j, k) in enumerate(zip(c, r), 1):
    if k > d[j][1]:
        d[j] = [idx, k]


if t in search:
    print(d[t][0])
else:
    print(d[c[0]][0])
