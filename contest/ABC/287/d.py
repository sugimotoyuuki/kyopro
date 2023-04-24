word = list(input())
t = input()

tmp = str()
for i in range(len(word)):
    for letter in word:
        tmp += letter
    print(letter)
