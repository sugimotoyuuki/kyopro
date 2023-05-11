n = int(input())
a = list(map(int, input().split()))
q = int(input())
que_list = [list(map(int, input().split())) for _ in range(q)]

for que in que_list:
    k = que[1] - 1
    if que[0] == 1:
        a[k] = que[2]
    else:
        print(a[k])
