n = int(input())
a = list(map(int, input().split()))

min_div2_count, min_div3_count, total = 100, 100, 0
s = set()
for i in range(n):
    div2_count = 0
    div3_count = 0
    while True:
        if a[i] % 2 == 0:
            a[i] //= 2
            div2_count += 1
            total += 1
        elif a[i] % 3 == 0:
            a[i] //= 3
            div3_count += 1
            total += 1
        else:
            s.add(a[i])
            min_div2_count = min(min_div2_count, div2_count)
            min_div3_count = min(min_div3_count, div3_count)
            break

if len(s) == 1:
    return_val = n * (min_div2_count + min_div3_count)  # リストに対して数字を何回かけて戻すか
    print(total - return_val)
else:
    print(-1)
