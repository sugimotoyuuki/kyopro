def remaining_cookies(H, W, cookies):
    while True:
        to_remove = set()
        for i in range(H):
            row = [cookies[i][j] for j in range(W) if cookies[i][j] is not None]
            if len(row) >= 2 and len(set(row)) == 1:
                for j in range(W):
                    if cookies[i][j] is not None:
                        to_remove.add((i, j))

        for j in range(W):
            col = [cookies[i][j] for i in range(H) if cookies[i][j] is not None]
            if len(col) >= 2 and len(set(col)) == 1:
                for i in range(H):
                    if cookies[i][j] is not None:
                        to_remove.add((i, j))

        if to_remove:
            for i, j in to_remove:
                cookies[i][j] = None
        else:
            break

    count = sum(1 for i in range(H) for j in range(W) if cookies[i][j] is not None)
    return count


h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]

print(remaining_cookies(h, w, g))
