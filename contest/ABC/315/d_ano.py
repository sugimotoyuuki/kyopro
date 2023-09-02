h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]
removed_rows = set()
removed_cols = set()

while True:
    row_set = set()
    col_set = set()

    # 各行を確認
    for i in range(h):
        if i not in removed_rows:
            row = [g[i][j] for j in range(w) if j not in removed_cols]
            if len(row) >= 2 and len(set(row)) == 1:
                row_set.add(i)

    # 各列を確認
    for j in range(w):
        if j not in removed_cols:
            col = [g[i][j] for i in range(h) if i not in removed_rows]
            if len(col) >= 2 and len(set(col)) == 1:
                col_set.add(j)

    removed_rows.update(row_set)
    removed_cols.update(col_set)
    if not row_set and not col_set:
        break

ans = (h - len(removed_rows)) * (w - len(removed_cols))
print(ans)
