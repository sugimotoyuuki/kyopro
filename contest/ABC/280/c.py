s = input()
t = input()

for i in range(len(t)):
    try:
        if s[i] != t[i]:
            print(i + 1)
            exit()
    except IndexError:
        print(i + 1)
