from functools import lru_cache


@lru_cache(maxsize=1000)
def dfs(num):
    if num == 0:
        return 1
    else:
        return dfs(num // 2) + dfs(num // 3)


n = int(input())
ans = dfs(n)
print(ans)
