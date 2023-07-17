s = list(map(int, input().split()))

for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        print("No")
        exit()
for el in s:
    if not (100 <= el and el <= 675):
        print("No")
        exit()
    if el % 25 != 0:
        print("No")
        exit()

print("Yes")
