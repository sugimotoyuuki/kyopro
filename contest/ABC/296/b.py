s = [list(input()) for _ in range(8)]

idx = [[0] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        idx[i][j] = chr(97 + j) + str(8 - i)

for row_s, row_idx in zip(s, idx):
    for el_s, el_idx in zip(row_s, row_idx):
        if el_s == "*":
            print(el_idx)
