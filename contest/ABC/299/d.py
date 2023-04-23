n = int(input())

left = 1
right = n
for _ in range(20):
    if left == right - 1:
        print(f"! {right - 1}")
        exit()

    mid = (left + right) // 2
    print(f"? {mid}")
    s = input()
    if s == "0":
        left = mid
    else:
        right = mid
