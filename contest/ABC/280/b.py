n = int(input())
s = list(map(int, input().split()))
sum_s = [0] * n
sum_s[0] = s[0]

for i in range(1, n):
    sum_s[i] = s[i] - s[i - 1]

print(*sum_s)
