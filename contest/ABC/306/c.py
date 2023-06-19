n = int(input())
a = list(map(int, input().split()))

s = set()
ans = list()
for el in a:
    if el in s:
        ans.append(el)
        s.remove(el)
    else:
        s.add(el)

print(*ans)
