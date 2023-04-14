# input
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

n = h + w - 2

# bitsには縦を1, 横を0としたときそれぞれ2つずつ持っているような2進数を入れる
bits = list()
for bit in range(1 << n):
    bit_list = list(format(bit, "b"))
    if sum(map(int, bit_list)) == h - 1:
        bits.append(bit)

ans = 0
for bit in bits:
    posx, posy = 0, 0
    path = {a[posx][posy]}
    for i in range(n):
        if bit & (1 << i):
            path.add(a[posy + 1][posx])
            posy += 1
        else:
            path.add(a[posy][posx + 1])
            posx += 1

    # print(path)
    if len(path) == n + 1:
        ans += 1

print(ans)
