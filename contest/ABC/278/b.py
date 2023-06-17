# 時間hと分mを1づつイテレートして、それぞれ24時間、60分になると0に戻るようにする。
def iterate_time(hour, min):
    if min < 60:
        min += 1
    elif h < 23:
        hour += 1
        min = 0
    else:
        hour = 0
        min = 0
    return hour, min


h, m = map(int, input().split())

# 解説
# 1. 1づつイテレートして、それぞれ24時間、60分になると0に戻るようにする。
# 2. それぞれの桁を文字列に変換して、2桁になるようにする。
# 3. 2桁の文字列を結合して、int型に変換する。
# 4. 3で得られた値が24時間、60分を超えていないかチェックする。
# 5. 超えていなければ、その値を出力して終了する。
# 6. 超えていれば、1に戻る。
while True:
    str_h = str(h)
    str_m = str(m)
    if len(str_h) == 1:
        str_h = "0" + str_h
    if len(str_m) == 1:
        str_m = "0" + str_m
    if int(str_h[0] + str_m[0]) < 24 and int(str_h[1] + str_m[1]) < 60:
        print(h, m)
        exit()
    else:
        h, m = iterate_time(h, m)
