n = int(input())
if n % 2 == 1:
    exit()
m = n // 2

ans_list = []
for bit in range(1 << n):
    tmp = ""
    cnt = 0
    for i in range(n):
        if cnt < 0:
            continue
        if bit & (1 << i):
            tmp += "("
            cnt += 1
        else:
            tmp += ")"
            cnt -= 1
    if cnt == 0:
        ans_list.append(tmp)

ans_list.sort()
for ans in ans_list:
    print(ans)
