import math

a, b = map(int, input().split())

n = ((a / (2 * b)) ** 2) ** (1 / 3)
x1 = math.floor(n)
x2 = math.ceil(n)
tmp1, tmp2 = float("inf"), float("inf")
if x1 > 0:
    tmp1 = b * (x1 - 1) + a / (x1**0.5)
if x2 > 0:
    tmp2 = b * (x2 - 1) + a / (x2**0.5)
ans = min(tmp1, tmp2)
print(ans)
