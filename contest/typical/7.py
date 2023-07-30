from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())


ans = 0
for _ in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    if idx == 0:
        ans = abs(a[idx] - b)
    elif idx == n:
        ans = abs(a[idx - 1] - b)
    else:
        ans = min(abs(a[idx] - b), abs(a[idx - 1] - b))
    print(ans)
