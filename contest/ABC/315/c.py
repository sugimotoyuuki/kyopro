n = int(input())
fs = [list(map(int, input().split())) for _ in range(n)]
fs.sort(key=lambda x: x[1], reverse=True)
max_f, max_s = fs[0]
fs[0] = [-float("inf"), -float("inf")]
same_s, ano_s = 0, 0
for f, s in fs:
    if f == max_f:
        same_s = max(same_s, s)
    else:
        ano_s = max(ano_s, s)

print(max_s + max(same_s // 2, ano_s))
