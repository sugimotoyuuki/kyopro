n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = []
for el_a in a:
    p.append((el_a, 0))
for el_b in b:
    p.append((el_b + 1, 1))
p.sort(key=lambda x: x[0])

a_amount = 0
b_amount = m

for el in p:
    if p[1] == 0:
        a_amount += 1
    else:
        b_amount -= 1
    if a_amount >= b_amount:
        print(el[0])
        exit()
