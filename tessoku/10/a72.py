import copy

h, w, k = map(int, input().split())
C = [list(input()) for _ in range(h)]

# 黒を1に白を0にする
for i, row in enumerate(C):
    for j, el in enumerate(row):
        if el == "#":
            C[i][j] = 1
        else:
            C[i][j] = 0

ans = -1
# 行を全探索、列を白が多い順に当てはめていく
for bit in range(1 << h):
    # 行列の初期化
    D = copy.deepcopy(C)
    lim = 0

    # bitに該当する列を黒塗りする
    for i in range(h):
        if bit & (1 << i):
            if lim >= k:
                break
            D[i] = list(map(lambda x: x or 1, D[i]))
            lim += 1

    # 各列の黒の数を求める
    sum_cols = list()
    for j in range(w):
        sum_col = 0
        for i in range(h):
            sum_col += D[i][j]
        sum_cols.append((j, sum_col))

    # 黒の数を少ない順に並べ、塗り替える
    sum_cols.sort(key=lambda x: x[1])
    for sum_col in sum_cols:
        if lim >= k:
            break
        for d in D:
            d[sum_col[0]] = 1
        lim += 1

    ans = max(sum(map(sum, D)), ans)

print(ans)
