k = int(input())
lim = int(k**0.5) + 1
ans = 1

for p in range(2, lim):
    e = 0
    while k % p == 0:
        k //= p
        e += 1
    n = 0
    while e > 0:
        n += p
        x = n
        while x % p == 0:
            x //= p
            e -= 1
    ans = max(ans, n)
ans = max(ans, k)

print(ans)
