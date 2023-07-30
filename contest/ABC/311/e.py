h, w, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]


def count_squares(n, m):
    return sum((n - i) * (m - i) for i in range(min(n, m)))


print(count_squares(2, 4))  # Output: 8
