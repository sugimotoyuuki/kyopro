D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]
M = int(input())

sc = sum(C)
for _ in range(M):
    d, q = map(int, input().split())
    t[d - 1] = q
    ans, tmp = 0, 0
    last = [0] * 26
    for i in range(D):
        tmp += sc - C[t[i] - 1] * (i + 1 - last[t[i] - 1])  # 全体からその日の満足度を減らす
        ans += S[i][t[i] - 1] - tmp
        last[t[i] - 1] = i + 1
    print(ans)
