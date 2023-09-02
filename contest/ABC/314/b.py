from collections import defaultdict

n = int(input())

c_list = []
a_list = []
for _ in range(n):
    c = int(input())
    c_list.append(c)
    a = set(map(int, input().split()))
    a_list.append(a)

x = int(input())

d = defaultdict(list)
for i in range(n):
    if x in a_list[i]:
        d[c_list[i]].append(i + 1)

if d:
    print(len(d[min(d)]))
    print(*d[min(d)])
else:
    print(0)
    print("")
