# ハッシュでも解けます
s = list(input())

# 0列目から順番に足していくため、一つ余分に行を作る
# 行が0 ~ 9, 列が何番目の桁か
count_dig = [[0] * 10 for _ in range(len(s) + 1)]

for i, el in enumerate(s):
    count_dig[i + 1] = count_dig[i].copy()
    count_dig[i + 1][int(el)] ^= 1  # 0 ~ 9が偶数個なら0、奇数個なら1

d = dict()
for row in count_dig:
    row = tuple(row)
    if row not in d.keys():
        d[row] = 1
    else:
        d[row] += 1

# 選びうる数はnC2より n * (n - 1) // 2をansに足していく
ans = 0
for n in d.values():
    ans += n * (n - 1) // 2

print(ans)
