n = int(input())
a = list(map(int, input().split()))

s = set()
ans = 0
count = 0
for i in range(n):
    idx = i + 1
    if idx == a[i]:
        ans += count
        count += 1
        continue
    if idx > a[i]:
        tmp = (idx, a[i])
    elif a[i] > idx:
        tmp = (a[i], idx)
    if tmp in s:
        ans += 1
    else:
        s.add(tmp)
print(ans)
