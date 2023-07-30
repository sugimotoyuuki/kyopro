n = int(input())
a = list(map(int, input().split()))
g = {i: [] for i in range(1, n + 1)}
for i, ai in enumerate(a, 1):
    g[i].append(ai)


path = [1]
seen = [False] * (n + 1)
st = [1]
seen[1] = True
while True:
    k = st.pop()
    for el in g[k]:
        if seen[el] is True:
            idx = path.index(el)
            ans = path[idx:]
            print(len(ans))
            exit(print(*ans))
        path.append(el)
        st.append(el)
        seen[el] = True
