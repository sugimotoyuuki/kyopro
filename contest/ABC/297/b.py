# input
s = input()

idx = {"K": [], "R": [], "B": []}
for i, w in enumerate(s):
    if w == "K":
        idx[w].append(i + 1)
    if w == "R":
        idx[w].append(i + 1)
    if w == "B":
        idx[w].append(i + 1)

ans = False
if idx["R"][0] < idx["K"][0] and idx["K"][0] < idx["R"][1]:
    if idx["B"][0] % 2 == 1 and idx["B"][1] % 2 == 0:
        print("Yes")
    elif idx["B"][0] % 2 == 0 and idx["B"][1] % 2 == 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
