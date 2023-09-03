from pprint import pprint


h, w = map(int, input().split())
row = [[0] * 26 for _ in range(h)]
col = [[0] * 26 for _ in range(w)]

# 列、行ごとに、各文字が何個含まれるかを数える
for i in range(h):
    c = list(input())
    for j, el in enumerate(c):
        row[i][ord(el) - 97] += 1
        col[j][ord(el) - 97] += 1

c_h, c_w = h, w
f_row = [False] * h
f_col = [False] * w


for _ in range(h + w):
    u_row, u_col = [], []

    # 行方向でアルファベットの数が、c_wと等しいところを探し、u_rowにインデックスを格納
    for i in range(h):
        if f_row[i]:
            continue
        for j in range(26):
            if row[i][j] == c_w and c_w >= 2:
                u_row.append((i, j))

    # 列方向でアルファベットの数が、c_hと等しいところを探し、u_rowにインデックスを格納
    for i in range(w):
        if f_col[i]:
            continue
        for j in range(26):
            if col[i][j] == c_h and c_h >= 2:
                u_col.append((i, j))

    # jはアルファベットの番号と一致している
    # 格納したインデックスを展開する。一行まるまる消えたので、すべての列からそのアルファベットの数を1引く
    for i, j in u_row:
        for k in range(w):
            col[k][j] -= 1
        f_row[i] = True
        c_h -= 1

    for i, j in u_col:
        for k in range(h):
            row[k][j] -= 1
        f_col[i] = True
        c_w -= 1

pprint(c_h * c_w)
