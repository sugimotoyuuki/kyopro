import bisect

n = int(input())
a = list(map(int, input().split()))


def f(idx, pos):
    if idx % 2 == 0:
        return sleep[idx - 1] + (pos - a[idx - 1])
    else:
        return sleep[idx - 1]


sleep = [0] * (n)
for i in range(1, n):
    if i % 2 == 0:
        sleep[i] = sleep[i - 1] + a[i] - a[i - 1]
    else:
        sleep[i] = sleep[i - 1]

q = int(input())
for _ in range(q):
    left, right = map(int, input().split())
    l_idx = bisect.bisect_right(a, left)
    r_idx = bisect.bisect_right(a, right)
    f_l = f(l_idx, left)
    f_r = f(r_idx, right)
    ans = f_r - f_l
    print(ans)
