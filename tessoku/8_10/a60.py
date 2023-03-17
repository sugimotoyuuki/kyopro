from collections import deque

N = int(input())
A = list(map(int, input().split()))

S = deque()
ans = list()

print(-1)
for i in range(1, N):
    S.append((i, A[i - 1]))
    while len(S) >= 1:
        if S[-1][1] <= A[i]:
            S.pop()
        else:
            break
    if len(S) >= 1:
        print(S[-1][0])
    else:
        print(-1)
