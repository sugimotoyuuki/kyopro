from functools import lru_cache

s = input()


@lru_cache(maxsize=1000)
def fib(i, j):
    if i == j:
        return int(s[i - 1])
    else:
        return fib(i, j - 1) + fib(i, j - 1)
