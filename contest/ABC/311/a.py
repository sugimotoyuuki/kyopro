n = int(input())
s = input()
abc = set()

for i, el in enumerate(s, 1):
    abc.add(el)
    if abc == {"A", "B", "C"}:
        print(i)
        exit()
