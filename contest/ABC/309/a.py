a, b = map(int, input().split())

d = {1: {2}, 2: {1, 3}, 3: {2}, 4: {5}, 5: {4, 6}, 6: {5}, 7: {8}, 8: {7, 9}, 9: {8}}

if b in d[a]:
    print("Yes")
else:
    print("No")
