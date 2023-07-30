from collections import defaultdict
from bisect import bisect_left

(
    h,
    w,
    pos_r,
    pos_c,
) = map(int, input().split())
n = int(input())

row_kabe = defaultdict(list)
col_kabe = defaultdict(list)
for _ in range(n):
    r, c = map(int, input().split())
    row_kabe[r].append(c)
    col_kabe[c].append(r)
for k in row_kabe.keys():
    row_kabe[k].sort()
for k in col_kabe.keys():
    col_kabe[k].sort()

q = int(input())
dr = [list(input().split()) for _ in range(q)]


for dir, rep in dr:
    rep = int(rep)
    if dir == "L":
        if row_kabe[pos_r]:
            tmp = bisect_left(row_kabe[pos_r], pos_r)
            if row_kabe[pos_r][tmp] < pos_c - rep:
                if pos_c - rep <= 1:
                    pos_c = 1
                else:
                    pos_c -= rep
            else:
                pos_c = row_kabe[pos_r][tmp] + 1
        else:
            pos_c -= rep
    elif dir == "R":
        if row_kabe[pos_r]:
            tmp = bisect_left(row_kabe[pos_r], pos_r)
            if row_kabe[pos_r][tmp] > pos_c + rep:
                if pos_c + rep >= w:
                    pos_c = w
                pos_c += rep
            else:
                pos_c = row_kabe[pos_r][tmp] - 1
        else:
            pos_c += rep
    elif dir == "U":
        if col_kabe[pos_c]:
            tmp = bisect_left(col_kabe[pos_c], pos_c)
            if col_kabe[pos_c][tmp] < pos_r - rep:
                if pos_r - rep <= 1:
                    pos_r = 1
                pos_r -= rep
            else:
                pos_r = col_kabe[pos_c][tmp] + 1
        else:
            pos_r -= rep
    elif dir == "D":
        if col_kabe[pos_c]:
            tmp = bisect_left(col_kabe[pos_c], pos_c)
            if col_kabe[pos_c][tmp] > pos_r + rep:
                if pos_r + rep >= h:
                    pos_r = h
                pos_r += rep
            else:
                pos_r = col_kabe[pos_c][tmp] - 1
        else:
            pos_r += rep
    print(pos_r, pos_c)
