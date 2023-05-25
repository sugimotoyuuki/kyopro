n = int(input())
s = input()

taka = list()
ao = list()
for i, letter in enumerate(s):
    if letter == "T":
        taka.append(i)
    else:
        ao.append(i)

if len(taka) > len(ao):
    print("T")
elif len(taka) < len(ao):
    print("A")
else:
    if taka[-1] > ao[-1]:
        print("A")
    else:
        print("T")
