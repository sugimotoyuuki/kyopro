n, m = map(int, input().split())
pcf = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        p1, c1, *f1 = pcf[i]
        p2, c2, *f2 = pcf[j]
        f1 = set(f1)
        f2 = set(f2)
        if p1 >= p2 and f2 >= f1 and (p1 > p2 or len(f2 - f1) > 0):
            print("Yes")
            exit()
print("No")
