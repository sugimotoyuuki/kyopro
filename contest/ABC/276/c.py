from bisect import bisect_right

n = int(input())
a = list(map(lambda x: int(x), input().split()))


q = []
q.append(a.pop())
while True:
    if min(q) < a[-1]:
        tmp = a.pop()
        q.sort()
        a.append(q.pop(bisect_right(q, tmp) - 1))
        q.append(tmp)
        q.sort()
        while q:
            a.append(q.pop())
        break
    q.append(a.pop())

print(*a)
