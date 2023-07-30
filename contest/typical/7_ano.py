from bisect import bisect_right

n = int(input())
# この処理のお陰で境界値の処理が必要なくなる
alst = list(map(int, input().split())) + [-(10**20)] + [10**20]
alst.sort()

Q = int(input())
for _ in range(Q):
    b = int(input())
    pos = bisect_right(alst, b)
    print(min(b - alst[pos - 1], alst[pos] - b))
