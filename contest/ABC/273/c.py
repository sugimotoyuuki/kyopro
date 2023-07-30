from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = set(a)
b = sorted(list(b))


ans = [0] * len(a)
for el in a:
    ans[len(b) - bisect_left(b, el) - 1] += 1

for a in ans:
    print(a)
