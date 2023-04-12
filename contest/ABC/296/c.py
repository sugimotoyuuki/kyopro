# input
n, x = map(int, input().split())
a = set(map(int, input().split()))

for i in a:
    if i + x in a:
        print("Yes")
        exit(0)

print("No")
