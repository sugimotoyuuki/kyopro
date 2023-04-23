n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())

dp = [0] * (x + 1)
dp[x] = 1

for i in range(x, 0, -1):
    for down in a:
        if dp[i] == 1 and (i - down) not in b:
            if i - down >= 0:
                dp[i - down] = 1

print("Yes") if dp[0] else print("No")
