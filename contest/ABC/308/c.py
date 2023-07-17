from functools import cmp_to_key


def cmp(a, b):
    if a[0] * b[1] == a[1] * b[0]:
        return 0
    # aがbより大きいとき、aを前にしたいため-1を返す
    return -1 if a[0] * b[1] > a[1] * b[0] else 1


n = int(input())
tos = []
for i in range(1, n + 1):
    a, b = map(int, input().split())
    tos.append((a, a + b, i))

tos.sort(key=cmp_to_key(cmp))
ans_list = list()
for el in tos:
    ans_list.append(el[2])
print(*ans_list)
