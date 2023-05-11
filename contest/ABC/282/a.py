k = int(input())
alp = list()

for i in range(k):
    alp.append(chr(65 + i))

print(*alp, sep="")
