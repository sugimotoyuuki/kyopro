import math

# input
n = int(input())

ans = 0
for i in range(1, n):
    ab, cd = i, n - i
    # sqrtを切り捨てた値まで調べる
    lim_ab = math.floor(math.sqrt(ab))
    lim_cd = math.floor(math.sqrt(cd))

    count_ab, count_cd = 0, 0
    for j in range(1, lim_ab + 1):
        if ab % j == 0:
            count_ab += 2
            if ab == j * j:  # 2乗のときは場合の数が1
                count_ab -= 1

    for j in range(1, lim_cd + 1):
        if cd % j == 0:
            count_cd += 2
            if cd == j * j:
                count_cd -= 1

    ans += count_ab * count_cd


print(ans)
