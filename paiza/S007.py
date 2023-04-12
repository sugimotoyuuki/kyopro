import re

S = input()
num = list(re.sub(r"\D", "", S))
s = re.sub(r"[0-9]+\(", r"(", S)

alp = dict()
for i in range(26):
    alp[chr(97 + i)] = 0

p1count = 0
p2count = 0
mag = 0
multi = list()
tmp = list()
for el in s:
    if el == "(":
        multi.append(num[p1count])
        p1count += 1
        sum = list(map(lambda x: x * mag, multi))
        for t in tmp:
            alp[t] += sum
        tmp = list()
    elif el == ")":
        multi.pop()
        sum = list(map(lambda x: x * mag, multi))
        for t in tmp:
            alp[t] += sum
        tmp = list()

    if str.isnumeric(el):
        mag = int(el)
        sum = list(map(lambda x: x * mag, multi))
        for t in tmp:
            alp[t] += sum
        tmp = list()
    elif el != "(" and el != ")":
        tmp.append(el)


print(s)
