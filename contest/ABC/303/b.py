w, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
rel = [set() for _ in range(w + 1)]

for i in range(h):
    for j in range(1, w):
        rel[a[i][j]].add(a[i][j - 1])
        rel[a[i][j - 1]].add(a[i][j])

ans = 0
for i, r in enumerate(rel):
    if i == 0:
        continue
    if len(r) < w:
        ans += w - 1 - len(r)
print(ans // 2)
