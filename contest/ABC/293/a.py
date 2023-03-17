S = list(input())
for i in range(0, int(len(S)), 2):
    tmp = S[i]
    S[i] = S[i + 1]
    S[i + 1] = tmp

print("".join(S))
