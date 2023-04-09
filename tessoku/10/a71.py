# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
A.sort()
B.sort(reverse=True)
for a, b in zip(A, B):
    ans += a * b

print(ans)
