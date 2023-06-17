n = int(input())

if n <= 999:
    print(n)
    exit()

str = "9999"
while True:
    if n <= int(str):
        dig = len(str) - 3
        print(int(n // 10**dig * 10**dig))
        exit()
    else:
        str += "9"
