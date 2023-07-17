n, m = map(int, input().split())
a = sorted(map(int, input().split()))

tmp = a[0]
tables = []
for i in range(n - 1):
    if a[i + 1] > a[i] + 1:
        tables.append(tmp)
        tmp = 0
    tmp += a[i + 1]
tables.append(tmp)
if a[0] == (a[-1] + 1) % m and len(tables) > 1:
    tables[0] += tables[-1]

total = sum(a)
table = max(tables)
print(total - table)
