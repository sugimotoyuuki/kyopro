s = input()
t = input()
m = len(t)
n = len(s) - m + 1
if n < 0:
    print("No")
    exit()

for i in range(n):
    if t == s[i : i + m]:
        print("Yes")
        exit()

print("No")
