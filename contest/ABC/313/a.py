n = int(input())
p = list(map(int, input().split()))

max_ = -float("inf")
idx = 0
for i in range(n):
    if p[i] >= max_:
        max_ = p[i]
        idx = i

if idx == 0:
    print(0)
else:
    print(p[idx] + 1 - p[0])
