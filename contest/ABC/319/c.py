from itertools import permutations


c = [list(map(int, input().split())) for _ in range(3)]
c = sum(c, [])

# 横縦斜め
cand = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check(p):
    for idx in range(8):
        # 各列のすべての選び方を試し、がっかりかがっかりではないか確かめる
        for i, j, k in permutations(cand[idx]):
            # i, j を先に開け、kを最後に開けるのであればがっかり
            if c[i] == c[j] and p[i] < p[k] and p[j] < p[k]:
                return False
    return True


# permutations(range(9)) はどういう順番で開けるかということ
# p = [1, 0, 2]とあったとき、c[1] -> c[0] -> c[2]の順で選ぶということ
print(sum(check(p) for p in permutations(range(9))) / 362880)
