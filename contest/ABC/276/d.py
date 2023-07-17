from math import gcd

n = int(input())
a = list(map(int, input().split()))

g = 0
# すべての要素の最大公約数を求めてしまう
for el in a:
    g = gcd(g, el)

# 求めた最大公約数で割ったときに2,3で割れる回数を求める
count = 0
for el in a:
    tmp = el // g
    while tmp % 2 == 0:
        tmp //= 2
        count += 1
    while tmp % 3 == 0:
        tmp //= 3
        count += 1
    if tmp != 1:
        print(-1)
        exit()
print(count)
