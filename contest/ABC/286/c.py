from collections import deque

n, a, b = map(int, input().split())
s = deque(list(input()))

ans = float("inf")
for i in range(n):
    value = 0
    if i != 0:
        s.append(s.popleft())
    value += a * i
    for j in range(n // 2):
        if s[j] != s[n - j - 1]:
            value += b

    ans = min(ans, value)

print(ans)
