n, yl = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))


def check(x):
    cnt, cut = 0, 0
    for i in range(n):
        if a[i] - cut >= x and yl - a[i] >= x:
            cnt += 1
            cut = a[i]
    return cnt >= k


left, right = 0, yl
while left < right:
    mid = (left + right + 1) // 2
    # midが条件を満たすなら、midが切れるので右側の範囲へ移動
    # midが条件を満たさないなら、midは切れないので左側の範囲へ移動
    if check(mid):
        left = mid
    else:
        right = mid - 1

print(left)  # leftは切れるものの最大値
