import sys

# input
N = int(input())
W = list(input().split())
term = ["and", "not", "that", "the", "you"]

for w in W:
    if w in term:
        print("Yes")
        sys.exit(0)
print("No")
