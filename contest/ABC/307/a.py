n = int(input())
a = list(map(int, input().split()))

m = len(a) // n

ans = []
tmp1 = 0
tmp2 = 0
for i, el in enumerate(a):
    if tmp1 < m:
        tmp1 += 1
        tmp2 += el
    else:
        ans.append(tmp2)
        tmp1 = 1
        tmp2 = el
ans.append(tmp2)
print(*ans)
