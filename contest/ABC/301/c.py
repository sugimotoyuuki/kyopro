replace = ("a", "t", "c", "o", "d", "e", "r")
s = input()
t = input()


num_s = {chr(i): 0 for i in range(97, 123)}
num_t = {chr(i): 0 for i in range(97, 123)}
num_s["@"] = 0
num_t["@"] = 0

n = len(s)
for i, j in zip(s, t):
    num_s[i] += 1
    num_t[j] += 1

for i in range(97, 123):
    if num_s[chr(i)] > num_t[chr(i)]:
        if chr(i) not in replace:
            print("No")
            exit()
        num_t["@"] -= abs(num_s[chr(i)] - num_t[chr(i)])
    elif num_s[chr(i)] < num_t[chr(i)]:
        if chr(i) not in replace:
            print("No")
            exit()
        num_s["@"] -= abs(num_s[chr(i)] - num_t[chr(i)])
    num_s[chr(i)] = 0
    num_t[chr(i)] = 0


if (num_s["@"] >= 0 and num_t["@"] >= 0) and num_s["@"] == num_t["@"]:
    print("Yes")
else:
    print("No")
