# d.png参照

s = input()
t = input()

s_size = len(s)
t_size = len(t)

match_list = [True]  # 最初は何も選んでないのでTrue
match = True
for i in range(t_size):
    if s[i] == t[i] or s[i] == "?" or t[i] == "?":
        match_list.append(match)
    else:
        match = False
        match_list.append(match)

rev_s = s[::-1]
rev_t = t[::-1]
rev_match_list = [True]
match = True
for i in range(t_size):
    if rev_s[i] == rev_t[i] or rev_s[i] == "?" or rev_t[i] == "?":
        rev_match_list.append(match)
    else:
        match = False
        rev_match_list.append(match)

for i in range(t_size + 1):
    if match_list[i] and rev_match_list[t_size - i]:
        print("Yes")
    else:
        print("No")
