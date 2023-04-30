h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]


for j in range(h + 1):
    if j != 0:
        a.append(a.pop(0))
    if a == b:
        print("Yes")
        exit()
    for k in range(w + 1):
        if k != 0:
            for i in range(h):
                a[i].append(a[i].pop(0))
        if a == b:
            print("Yes")
            exit()

print("No")
