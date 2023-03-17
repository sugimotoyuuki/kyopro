# input
N = int(input())
A = list(map(int, input().split()))
called = [False] * (N + 1)

for i in range(1, N + 1):
    if called[i] is False:
        called[A[i - 1]] = True

print(called.count(False) - 1)
ans = list()
for i in range(1, N + 1):
    if called[i] is False:
        ans.append(i)

print(*ans, sep=" ")
