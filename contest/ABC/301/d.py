s_bin = input()
n = int(input())

if int(s_bin) <= n:
    print(n)
    exit()

n_bin = format(n, "b")
for i, s_dig, n_dig in enumerate(zip(s_bin, n_bin)):
    if s_dig != n_dig:
        diff_dig = i
