def can_fit(width, L, M):
    lines = 1
    current_width = 0

    for el in L:
        add_width = el + 1 if current_width != 0 else el
        if current_width + add_width <= width:
            current_width += add_width
        else:
            lines += 1
            current_width = el

    return lines <= M


n, m = map(int, input().split())
l_list = list(map(int, input().split()))

low, high = max(l_list), sum(l_list) + n

while low < high:
    mid = (low + high) // 2
    if can_fit(mid, l_list, m):
        high = mid
    else:
        low = mid + 1

print(low)
