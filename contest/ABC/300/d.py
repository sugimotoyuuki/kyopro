def erastos(z):
    is_prime_list = ([False, True] * (z // 2 + 1))[0 : z + 1]
    is_prime_list[1] = False
    is_prime_list[2] = True
    lim = int(z**0.5)
    for i in range(3, lim + 1, 2):
        if is_prime_list[i] is False:
            continue
        for j in range(i * i, z + 1, i):
            is_prime_list[j] = False

    return is_prime_list


is_prime_list = erastos(300000)
prime_list = list()
for num, is_prime in enumerate(is_prime_list):
    if is_prime:
        prime_list.append(num)

n = int(input())
m = len(prime_list)
ans = 0
for i in range(m):
    k = m - 1
    for j in range(i + 1, m):
        while k > j:
            v = prime_list[i] ** 2 * prime_list[j]  # 最大10^5なので大丈夫
            if v > n:
                k -= 1
                continue
            v *= prime_list[k]
            if v > n:
                k -= 1
                continue
            v *= prime_list[k]
            if v > n:
                k -= 1
                continue
            break  # これら満たす最大のkが見つかったところでストップ
        else:
            break

        ans += k - j

print(ans)
