h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]

s_row = [[] for _ in range(w)]
t_row = [[] for _ in range(w)]
for i in range(h):
    for j in range(w):
        s_row[j].append(s[i][j])
        t_row[j].append(t[i][j])

s_row.sort()
t_row.sort()
if s_row == t_row:
    print("Yes")
else:
    print("No")
