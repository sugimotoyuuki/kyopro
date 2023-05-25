n = int(input())
a = list(map(int, input().split()))
insert = dict()
for i in range(1, n):
    if abs(a[i] - a[i - 1]) > 1:
        insert[i] = []
        if a[i] > a[i - 1]:
            for j in range(a[i - 1] + 1, a[i]):
                insert[i].append(j)
        elif a[i - 1] > a[i]:
            for j in range(a[i - 1] - 1, a[i], -1):
                insert[i].append(j)

ans = list()
for i, el in enumerate(a):
    if i in insert.keys():
        ans += insert[i]
    ans.append(el)

print(*ans)
