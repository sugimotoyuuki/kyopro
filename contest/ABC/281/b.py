s = list(input())
if len(s) == 8:
    try:
        if str(s[0]).isupper() and str(s[-1]).isupper():
            num = int("".join(list(s[1:7])))
            if num < 100000 or 999999 < num:
                print("No")
                exit()
            print("Yes")
        else:
            print("No")
    except ValueError:
        print("No")
else:
    print("No")
