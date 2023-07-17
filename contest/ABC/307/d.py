n = int(input())
s = list(input())

a = []
t = []
"""
文字を入れて行って、"("の数を保存、")"が来たら、
"("の数が0でなければ、"("までの文字を削除する
スライスを使ってしまうとコンテナ内の要素数nが計算量として加わるので、TLEする
"""
count = 0
for c in s:
    if c == ")" and count:
        while t[-1] != "(":
            t.pop()
        t.pop()
        count -= 1
    else:
        t.append(c)
        if c == "(":
            count += 1

print("".join(t))
