n, m = map(int, input().split())
s1 = [int(input()[3:]) for _ in range(n)]
s2 = {int(input()) for _ in range(m)}

count = 0
for s in s1:
    if s in s2:
        count += 1
print(count)
