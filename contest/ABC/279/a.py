s = input()

ans = 0
for letter in s:
    if letter == "v":
        ans += 1
    elif letter == "w":
        ans += 2

print(ans)
