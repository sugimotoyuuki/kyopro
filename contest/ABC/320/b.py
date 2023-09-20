s = input()
ans = 1
for i in range(len(s) + 1):
    for j in range(i + 1, len(s) + 1):
        if s[i:j] == s[i:j][::-1]:
            ans = max(ans, len(s[i:j]))

print(ans)
