from collections import defaultdict, deque

n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

d = defaultdict(deque)
for i in range(n):
    d[c[i]].append(s[i])

boo = [False] * (m + 1)
ans = []

for num in c:
    if boo[num]:
        ans.append(d[num].popleft())
    else:
        ans.append(d[num].pop())
        boo[num] = True

print("".join(ans))
