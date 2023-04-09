# input
n, d = map(int, input().split())
t = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        if t[j] - t[i] <= d:
            print(t[j])
            exit(0)

print(-1)
