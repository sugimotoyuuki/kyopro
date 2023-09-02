m = int(input())
d = list(map(int, input().split()))
center = (sum(d) + 1) // 2

cur = 0
for i in range(m):
    if cur + d[i] >= center:
        # 中央の値から先月の日数を引く
        day = center - cur
        print(i + 1, day)
        exit()
    cur += d[i]
