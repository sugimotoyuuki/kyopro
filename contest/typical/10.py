n = int(input())
scores = [[0] * 100001, [0] * 100001]

for i in range(1, n + 1):
    c, p = map(int, input().split())
    scores[c - 1][i] = p

for i in range(2, n + 1):
    scores[0][i] += scores[0][i - 1]
    scores[1][i] += scores[1][i - 1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(scores[0][r] - scores[0][l - 1], scores[1][r] - scores[1][l - 1])
