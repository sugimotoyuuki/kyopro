# input
N = int(input())
tmp = list(map(int, input().split()))

# B: iに対してどの部下を持つか
A = [-1] * (N + 1)
B = [list() for _ in range(N + 1)]
for i, t in enumerate(tmp, 2):
    A[i] = t
    B[A[i]].append(i)

count = [0] * (N + 1)
for i in range(N, 0, -1):
    for b in B[i]:
        count[i] += count[b]
    count[i] += len(B[i])

print(*count[1:])
