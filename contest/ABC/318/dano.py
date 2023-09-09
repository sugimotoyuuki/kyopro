#

n = 3
for bit in range((1 << n) - 1):
    s = set()
    for i in range(n):
        if not bit & (1 << i):  # フラグが立っているものは選ばない
            print(bit, 1 << i)
            s.add(i)
    print(s)
