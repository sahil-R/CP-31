matrix=[]
for i in range(3):
    matrix.append(list(map(int,input().split())))
solution = [[1 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        if matrix[i][j]%2==1:
            solution [i][j]=1^solution[i][j]
            # print(solution [i][j])
            #top
            if j-1>=0:
                solution[i][j-1]=1^solution[i][j-1]
                # print("top:",solution[i][j-1])
            #left
            if i-1>=0:
                solution[i-1][j]=1^solution[i-1][j]
                # print("left:",solution[i-1][j])
            #right
            if i+1<3:
                solution[i+1][j]=1^solution [i+1][j]
                # print(1^solution [i+1][j])
                # print("right:",solution[i+1][j])
            #bottom
            if j+1<3:
                solution[i][j+1]=1^solution [i][j+1]
                # print("bottom:",solution[i][j+1])
for i in range(len(matrix)):
    temp=[str(x) for x in solution[i]]
    print("".join(temp))