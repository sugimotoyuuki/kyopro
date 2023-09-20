from collections import deque

n = int(input())
a = list(map(int, input().split()))

a.sort()
a = deque(a)
m = [0] * n
for i in range(n):
    if i % 2 == 0:
        m[i] = a.popleft()

for i in range(n):
    if i % 2 == 1:
        m[i] = a.popleft()

for i in range(1, n - 1, 2):
    if not (m[i - 1] < m[i] and m[i + 1] < m[i]):
        exit(print("No"))
print("Yes")
