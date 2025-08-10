A = [[1, 2, 3]]

# 3x1 matrix
B = [[4],
     [5],
     [6]]

# Prepare an empty result matrix (1x1)
result = [[0]]

# Matrix multiplication using loops
for i in range(len(A)):              # Rows of A
    for j in range(len(B[0])):        # Columns of B
        for k in range(len(B)):       # Rows of B / Columns of A
            result[i][j] += A[i][k] * B[k][j]

print("Result of A x B:")
print(result)