d = dict(map(str.split, [*open(a := 0)][1:]))
while d:
    s, t = d.popitem()
    while t:  # tを始点として辞書に格納されているものを探索していく
        t = d.pop(t, 0)
        a |= s == t  # 一つでも一致するものがあれば1となる

print("YNeos"[a::2])
