n = int(input())
s = [input() for _ in range(n)]

m = len(s)
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        join = s[i] + s[j]
        kaibun = True
        t = len(join) // 2
        for k in range(t):
            if not (join[k] == join[len(join) - 1 - k]):
                kaibun = False
                break
        if kaibun:
            print("Yes")
            exit()
print("No")
