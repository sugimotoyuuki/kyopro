# input
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

answer = [[] for _ in range(H)]
for i in range(H):
    for a in A[i]:
        if a == 0:
            answer[i].append(".")
        else:
            answer[i].append(chr(64 + a))

for ans in answer:
    print(*ans, sep="")
