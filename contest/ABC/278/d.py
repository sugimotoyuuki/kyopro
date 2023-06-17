from collections import defaultdict

n = int(input())
a_list = list(map(int, input().split()))
a = {i + 1: a_list[i] for i in range(n)}
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

offset = 0
for q in query:
    if q[0] == 1:
        a = defaultdict(int)
        offset = q[1]
    elif q[0] == 2:
        a[q[1]] += q[2]
    elif q[0] == 3:
        diff = a.get(q[1], 0)
        print(diff + offset)
