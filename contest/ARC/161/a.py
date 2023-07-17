n = int(input())
a = list(map(int, input().split()))

# M型の数列sを作成
m = n // 2
a.sort()
s = [0] * len(a)
for i, el in enumerate(a):
    if i < m + 1:
        s[i * 2] = el
    else:
        s[i * 2 - n] = el

# sがM型かどうか判定
for i in range(1, len(s) - 1, 2):
    if not (s[i - 1] < s[i] and s[i] > s[i + 1]):
        print("No")
        exit()

print("Yes")
