D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

last = [0] * 27
ans = 0
for i in range(1, D + 1):
    t = int(input())
    last[t] = i
    sum_ = 0
    for j, el in enumerate(C, 1):
        sum_ += el * (i - last[j])
    ans += S[i - 1][t - 1] - sum_
    print(ans)
