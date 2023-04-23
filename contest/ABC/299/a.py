n = int(input())
s = input()

a = 0
for i in s:
    if i == "|":
        a += 1
    if a == 1 and i == "*":
        print("in")
        exit()

print("out")
