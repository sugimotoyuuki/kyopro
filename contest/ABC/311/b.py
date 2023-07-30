n, d = map(int, input().split())
s = [list(input()) for _ in range(n)]
count = 0
count_list = [0]
for j in range(d):
    b = True
    for i in range(n):
        if s[i][j] == "x":
            b = False
            count_list.append(count)
            count = 0
            break
    if b:
        count += 1
count_list.append(count)

print(max(count_list))
