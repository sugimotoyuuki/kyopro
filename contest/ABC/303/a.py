n = int(input())
s = input()
t = input()

for i, j in zip(s, t):
    if i != j:
        if (i == "1" and j == "l") or (i == "l" and j == "1"):
            continue
        elif (i == "0" and j == "o") or (i == "o" and j == "0"):
            continue
        else:
            print("No")
            exit()

print("Yes")
