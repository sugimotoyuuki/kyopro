from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)
n = int(input())
a = list(map(int, input().split()))

g = {i: [] for i in range(1, n + 1)}
for i, ai in enumerate(a, 1):
    g[i].append(ai)


def find_cycle(graph):
    color = defaultdict(int)
    cycle = []

    def dfs(node, path):
        color[node] = 1
        path.append(node)

        for neighbor in graph[node]:
            if color[neighbor] == 1:
                cycle.append(path[path.index(neighbor) :])
            elif color[neighbor] == 0:
                dfs(neighbor, path)

        path.pop()
        color[node] = 2

    for node in graph:
        if color[node] == 0:
            dfs(node, [])

    return cycle


cycle_path = find_cycle(g)
print(cycle_path)
