N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x):
    count, last = 0, 0
    for i in range(N):
        if A[i] - last >= x and L - A[i] >= x:
            count += 1
            last = A[i]

    return count >= K


left, right = 1, 1000000000
while left < right:
    mid = (left + right + 1) // 2
    ans = check(mid)
    if ans is True:
        left = mid
    else:
        right = mid - 1

print(left)
