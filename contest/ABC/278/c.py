# 数値n, qを受け取る
n, q = map(int, input().split())
# 数値t, a, bを1変数queryとして受け取る
query = [list(map(int, input().split())) for _ in range(q)]

ff = set()
for t, a, b in query:
    if t == 1:
        ff.add((a, b))
    elif t == 2:
        ff.discard((a, b))
    elif t == 3:
        if (a, b) in ff and (b, a) in ff:
            print("Yes")
        else:
            print("No")
