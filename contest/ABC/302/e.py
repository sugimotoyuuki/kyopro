N, Q = map(int, input().split())
g = [set() for _ in range(N)]
lens = [0] * N
ans = N
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u, v = q[1] - 1, q[2] - 1
        if lens[u] == 0:
            ans -= 1
        g[u].add(v)
        lens[u] += 1
        if lens[v] == 0:
            ans -= 1
        g[v].add(u)
        lens[v] += 1
    elif q[0] == 2:
        u = q[1] - 1
        if lens[u] == 0:
            print(ans)
            continue
        for v in g[u]:
            g[v].discard(u)
            lens[v] -= 1
            if lens[v] == 0:
                ans += 1
        g[u] = set()
        lens[u] = 0
        ans += 1
    print(ans)
