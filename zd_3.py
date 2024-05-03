def maxx(matr):
    for i in range(0,len(matr[0])):
        matr[0][i]=1
    for i in range(0,len(matr)):
        matr[i][0]=1
    for i in range(1,len(matr)):
        for j in range(1,len(matr[0])):
            matr[i][j]=matr[i-1][j]+matr[i][j-1]
    return matr[len(matr)-1][len(matr[0])-1]


matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(maxx(matrix))