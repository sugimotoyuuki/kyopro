t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    rank = [-1]
    for i in range(1, n + 1):
        rank.append((i, p[i - 1]))
    ans = []
    for i in range(1, n + 1):
        exist = True
        for j in range(1, n + 1):
            if i == j:
                continue
            # 往路で下の順位の人に抜かされているならば
            if (rank[i][0] < rank[j][0]) and (rank[i][1] > rank[j][1]):
                exist = False

        if exist:
            ans.append(i)

    print(len(ans))
