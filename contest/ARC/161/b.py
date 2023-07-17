n = int(input())

# 2^60から10^18になる
bin_set = [2**i for i in range(60)]


for _ in range(n):
    d = int(input())
    if d < 7:
        print(-1)
        continue
    ans = 0
    for i in range(d, 6, -1):
        count = 0
        for i, el in enumerate(b):
            print(i)
    # print(int("".join(b), 2))
