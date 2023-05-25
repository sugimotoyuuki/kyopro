hp, dmg = map(int, input().split())

if hp % dmg == 0:
    ans = hp // dmg
else:
    ans = hp // dmg + 1
print(ans)
