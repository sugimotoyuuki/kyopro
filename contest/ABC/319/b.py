n = int(input())

ans = []
for i in range(n + 1):
    found = False
    for j in range(1, 10):
        if n % j == 0 and i % (n // j) == 0:
            ans.append(str(j))
            found = True
            break
    if not found:
        ans.append("-")

print("".join(ans))
