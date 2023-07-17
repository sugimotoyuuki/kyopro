n = int(input())
b = bin(n)[2:]

ans = []
for i in range(len(b)):
    if i == 0:
        if b[i] == "1":
            ans.append("A")
        else:
            ans.append("B")
    else:
        if b[i] == "1":
            ans.append("B")
            ans.append("A")
        else:
            ans.append("B")

print(*ans, sep="")
