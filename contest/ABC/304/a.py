n = int(input())
query = [list(input().split()) for _ in range(n)]
num = float("inf")
for q in query:
    num = min(int(q[1]), num)

for i, q in enumerate(query):
    if int(q[1]) == num:
        idx = i

for i in range(idx, n):
    print(query[i][0])
for i in range(0, idx):
    print(query[i][0])
