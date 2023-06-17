p, q = input().split()
dist = [0, 3, 1, 4, 1, 5, 9]
for i in range(1, len(dist)):
    dist[i] = dist[i - 1] + dist[i]

idx1 = ord(p) - 65
idx2 = ord(q) - 65
ans = dist[idx2] - dist[idx1]
print(abs(ans))
