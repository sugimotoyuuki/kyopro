# input
N = int(input())
A = list(map(int, input().split()))

even = list()
for a in A:
    if a % 2 == 0:
        even.append(a)

print(*even)
