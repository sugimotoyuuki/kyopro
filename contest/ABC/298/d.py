from collections import deque


q = int(input())
num = deque([1])
ans = 1
mod = 998244353

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        num.append(query[1])
        ans = (ans * 10 + query[1]) % mod
    if query[0] == 2:
        front = num.popleft()
        ans -= pow(10, len(num), mod) * front
        ans %= mod
    if query[0] == 3:
        print(ans)
