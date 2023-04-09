a, b = map(int, input().split())
count = 0

if a < b:
    tmp = a
    a = b
    b = tmp
while b != 0:
    count += a // b
    a %= b
    if a < b:
        tmp = a
        a = b
        b = tmp


print(count - 1)
