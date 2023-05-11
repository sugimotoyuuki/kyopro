import bisect

n, t = map(int, input().split())
a = list(map(int, input().split()))
sum_a = [0]

for i, m_t in enumerate(a):
    sum_a.append(sum_a[i] + m_t)
t %= sum_a[-1]
index = bisect.bisect_left(sum_a, t)
ans = t - sum_a[index - 1]
print(index, ans)
