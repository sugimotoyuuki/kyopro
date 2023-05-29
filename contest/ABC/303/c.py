n, m, hp, k = map(int, input().split())
s = input()
xy = set(tuple(map(int, input().split())) for _ in range(m))

move = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
cur = (0, 0)
for w in s:
    cur = tuple(x + y for (x, y) in zip(cur, move[w]))
    hp -= 1
    if hp < 0:
        print("No")
        exit()
    elif hp < k:
        if cur in xy:
            xy.discard(cur)
            hp = k

print("Yes")
