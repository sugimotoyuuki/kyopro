from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

root = defaultdict(int)
cnt1 = 2
root[1] = 0
for i in a:
    root[cnt1] = root[i] + 1
    root[cnt1 + 1] = root[i] + 1
    cnt1 += 2

for i in range(1, len(root) + 1):
    print(root[i])
