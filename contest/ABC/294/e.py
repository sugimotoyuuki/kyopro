L, n1, n2 = map(int, input().split())

pressed = list()
n_list = [n1, n2]
for i, n in enumerate(n_list):
    t = 0
    for _ in range(n):
        v, rep = map(int, input().split())
        pressed.append([t, i, v])
        t += rep


pressed.sort()
# 最後のループを回す
pressed.append([L, 0, 0])

v12 = [0] * 2
ans = 0
pt = 0
# ptはtの前の時刻、まずv12に値を入れてそれらがあっていれば次のループのtからptを引く
for t, n, v in pressed:
    if v12[0] == v12[1]:
        ans += t - pt
    v12[n] = v
    pt = t

print(ans)
