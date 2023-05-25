from collections import deque


n, m, d = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
a = sorted(deque(a))
b = sorted(deque(b))

while a and b:
    if abs(a[-1] - b[-1]) <= d:
        print(a[-1] + b[-1])
        exit()
    if a[-1] > b[-1]:
        a.pop()
    else:
        b.pop()

print(-1)
