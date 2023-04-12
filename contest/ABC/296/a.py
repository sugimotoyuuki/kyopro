n = int(input())
s = list(input())

for i in range(1, n):
    if n == 1:
        print("Yes")
        exit(0)
    elif (s[i - 1] == "M" and s[i] == "M") or (s[i - 1] == "F" and s[i] == "F"):
        print("No")
        exit(0)

print("Yes")
