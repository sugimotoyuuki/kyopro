n = int(input())
ans = set()
for _ in range(n):
    s = input()
    if len(s) == 1:
        ans.add(s)
        continue
    rs = s[::-1]
    if (rs in ans) or (s in ans):
        continue
    else:
        ans.add(s)
print(len(ans))
