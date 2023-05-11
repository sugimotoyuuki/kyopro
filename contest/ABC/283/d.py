s = input()
bra_num = 0
d = dict()
double = set()

for let in s:
    if let == "(":
        bra_num += 1
        if bra_num not in d:
            d[bra_num] = []
    elif let == ")":
        if bra_num in d:
            double -= set(d[bra_num])
        d.pop(bra_num)
        bra_num -= 1
    elif let not in double:
        if bra_num in d:
            d[bra_num].append(let)
        double.add(let)
    else:
        print("No")
        exit()

print("No") if any(d) else print("Yes")
