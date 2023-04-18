n = int(input())
q = int(input())

boxes = [[] for _ in range(n + 1)]
numbers = dict()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        boxes[query[2]].append(query[1])
        if query[1] in numbers.keys():
            numbers[query[1]].add(query[2])
        else:
            numbers[query[1]] = set()
            numbers[query[1]].add(query[2])
    if query[0] == 2:
        print(*sorted(boxes[query[1]]))
    if query[0] == 3:
        print(*sorted(numbers[query[1]]))
