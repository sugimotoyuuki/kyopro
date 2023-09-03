N = int(input())
D = []  # D[i][j] will contain the distance from vertex i+1 to vertex j+1
for i in range(N - 1):
    row = list(map(int, input().split()))
    D.append(row)

# Initialize maximum weight variable
max_weight = 0

# Loop through the array to find the maximum weight
for i in range(N - 1):
    for j in range(len(D[i])):
        max_weight = max(max_weight, D[i][j])

print(max_weight)
