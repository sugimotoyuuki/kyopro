s = input()
n = int(input())

max_s = list()
for el in s:
    if el == "?":
        max_s.append("1")
    else:
        max_s.append(el)
max_s = int("".join(max_s), 2)

ans = list()
if n >= max_s:
    print(max_s)    
else:




