#  けんちょんの解説 https://drken1215.hatenablog.com/entry/2022/12/05/160400
k = int(input())
lim = int(k**0.5) + 1
ans = 0
for p in range(2, lim):
    print(p)
    e = 0
    # k に対して約数pがいくつあるかをaに入れている
    while k % p == 0:
        k //= p
        e += 1
    n = 0
    # 各p^e_iに対して最小のn!を求めていく、その中で最大値のものを選ぶ(最大値でなければmax(p^e_i)を含むことができない)
    while e > 0:
        n += p
        x = n
        while x % p == 0:  # 割れた数だけeを引く
            x //= p
            e -= 1
    ans = max(ans, n)
ans = max(ans, k)  # 素数の場合

print(ans)
