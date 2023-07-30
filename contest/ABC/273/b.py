n, k = map(int, input().split())

for i in range(1, k + 1):
    n = round(n + 0.5, -i)
print(int(n))
