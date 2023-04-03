# input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A.copy()
C.extend(B)
C.sort()

get_index = {c: i for i, c in enumerate(C, 1)}

ans = []
for a in A:
    ans.append(get_index[a])
print(*ans)

ans = []
for b in B:
    ans.append(get_index[b])
print(*ans)
