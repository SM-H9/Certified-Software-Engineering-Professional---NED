A = [[3,2,1],
     [1,2,3]]

B = [[1,2],
     [3,4],
     [5,6]]

product = [[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
           product [i][j] += A[i][k] * B[k][j] 


print(product)