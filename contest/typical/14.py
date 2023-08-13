# 配列が同じ大きさなのでできる
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

ans = 0
for el1, el2 in zip(a, b):
    ans += abs(el1 - el2)
print(ans)
