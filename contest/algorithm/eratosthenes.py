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


is_prime_list = erastos(30)
count = 0

prime_list = list()
for num, is_prime in enumerate(is_prime_list):
    if is_prime:
        prime_list.append(num)

print(prime_list)
