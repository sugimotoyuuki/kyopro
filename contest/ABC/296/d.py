import math

# input
n, m = map(int, input().split())
ans = int(2e18)

if n * n < m:
    print(-1)
    exit(0)

for a in range(1, math.ceil(math.sqrt(m)) + 1):
    b = math.ceil(m / a)
    if b <= n:
        ans = min(ans, a * b)
    if a > b:
        break

if ans == int(2e18):
    print(-1)
else:
    print(ans)
