t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    tar = n
    ans = []
    min_ = 0
    while tar:
        min_ += tar % 3
        tar //= 3
    if abs(n - k) % 2 == 0:
        print("Yes" if min_ <= k and k <= n else "No")
    else:
        print("No")
