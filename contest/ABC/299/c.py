n = int(input())
s = list(input())

count = 0
ans = 0
for idx, i in enumerate(s):
    if i == "o":
        count += 1
    if idx == n - 1 and "-" in set(s):
        if count > ans:
            ans = count
    if i == "-":
        if count > ans:
            ans = count
        count = 0

if ans:
    print(ans)
else:
    print("-1")
