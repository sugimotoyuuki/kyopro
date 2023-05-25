n, m = map(int, input().split())
a = list(map(int, input().split()))
b = a[::-1]
rev_list = list()
for i in range(n):
    for j in range(i, n):
        if i != j:
            tmp = a[:i] + b[n - 1 - j : n - i] + a[j + 1 :]
            rev_list.append(tmp)
        else:
            rev_list.append(a)
rev_list.sort()
print(*list(rev_list[m - 1]))
