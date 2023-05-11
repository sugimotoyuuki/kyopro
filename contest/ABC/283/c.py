s = input()

ans = 0
prev = False
n = len(s)
for i in range(n):
    if s[i] == "0":
        if prev is True:
            prev = False
            ans += 1
        elif i != n - 1 and s[i + 1] == "0":
            prev = True
        else:
            ans += 1
    else:
        ans += 1


print(ans)
