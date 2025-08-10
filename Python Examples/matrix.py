#tupples in matrix
matrix1 = [
    [10,20,30],
    [9,2,3]
    ]
matrix2 = [
    [10,42,30],
    [5,2,3]
    ]

sums = [[0,0,0],[0,0,0]]

for i in range (len(matrix1)):
    for j in range(len(matrix1[i])):
        sums[i][j] = matrix1[i][j] + matrix2[i][j]

print(sums)

for i in range (len(sums)):
    for j in range (len(sums[i])):
        print(f"sum[{i}][{j}] = {sums[i][j]} ", end="")
    print()