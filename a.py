import re

text = "この四角形の縦の長さは50m、横の長さは40mそして30kmの高さがあります。"

# 縦の長さを抽出
match_tate = re.search(r"縦.*?(\d+[\w]+)", text)
if match_tate:
    tate = match_tate.group(1)

# 横の長さを抽出
match_yoko = re.search(r"横.*?(\d+[\w]+)", text)
if match_yoko:
    yoko = match_yoko.group(1)

# 高さを抽出
match_takasa = re.search(r"(\d+[\w]+).*?高さ", text)
if match_takasa:
    takasa = match_takasa.group(1)

print(f"縦の長さ: {tate}")
print(f"横の長さ: {yoko}")
print(f"高さ: {takasa}")
