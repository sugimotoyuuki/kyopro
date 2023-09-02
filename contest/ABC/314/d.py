n = int(input())
s = list(input())
q = int(input())

lower_upper = 0
hoji = set()
for _ in range(q):
    t, x, c = input().split()
    t, x = int(t), int(x)
    if t == 1:
        s[x - 1] = c
        hoji.add(x - 1)
    elif t == 2:
        hoji = set()
        lower_upper = 2
    elif t == 3:
        hoji = set()
        lower_upper = 3

ans = []
if lower_upper == 0:
    print("".join(s))
    exit()
elif lower_upper == 2:
    for i, el in enumerate(s):
        if i not in hoji:
            ans.append(el.lower())
        else:
            ans.append(el)
elif lower_upper == 3:
    for i, el in enumerate(s):
        if i not in hoji:
            ans.append(el.upper())
        else:
            ans.append(el)

print("".join(ans))
