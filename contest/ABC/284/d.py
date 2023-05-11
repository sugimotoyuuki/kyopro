def erastos(z):
    is_prime_list = ([False, True] * (z // 2 + 1))[0 : z + 1]
    is_prime_list[1] = False
    is_prime_list[2] = True
    lim = int(z ** (1 / 2))  # min(p, q)の最小値は1/3まで求めれば良い
    for i in range(3, lim + 1, 2):
        if is_prime_list[i] is False:
            continue
        for j in range(i * i, z + 1, i):
            is_prime_list[j] = False

    return is_prime_list


T = int(input())
is_prime_list = erastos(2100000)
for _ in range(T):
    z = int(input())
    prime_list = list()
    for num, is_prime in enumerate(is_prime_list):
        if is_prime and z % num == 0:
            if z % num**2 == 0:
                q = int(z // num**2)
                print(num, q, sep=" ")
            else:
                p = int((z // num) ** 0.5)
                print(p, num, sep=" ")
            break
