s = list(input())
n = int(input())

m = len(s)
while True:
    tmp_s = s.copy()
    exist_q = False
    for i in range(m):
        if exist_q and s[i] == "?":
            tmp_s[i] = "0"
        elif s[i] == "?":
            tmp_s[i] = "1"
            top_num = i
            exist_q = True
    if not exist_q:
        if n >= int("".join(tmp_s), 2):
            exit(print(int("".join(tmp_s), 2)))
        else:
            exit(print(-1))
    if n >= int("".join(tmp_s), 2):
        s[top_num] = "1"
    else:
        s[top_num] = "0"
