n = input()
a = list(map(int, input().split()))
if len(a) == 1:
    exit(print(0))

a.sort()
sum_ = sum(a)
div = sum_ // len(a)
rem = sum_ % len(a)
b = [div] * len(a)
for i in range(len(b) - rem, len(b)):
    b[i] += 1

ans = 0
for i, j in zip(a, b):
    if i - j >= 0:
        ans += i - j
print(ans)
