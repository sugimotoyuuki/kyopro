n = int(input())
s = list(input())

par = False
for i, let in enumerate(s):
    if let == '"':
        par = not par
    if not par and let == ",":
        s[i] = "."

print(*s, sep="")
