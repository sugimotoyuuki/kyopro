# input
n = int(input())
a = list(map(int, input().split()))
a_dict = dict()
for el in a:
    if el not in a_dict.keys():
        a_dict[el] = 1
    else:
        a_dict[el] += 1

ans = 0
for v in a_dict.values():
    ans += v // 2


print(ans)
