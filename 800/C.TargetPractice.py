t=int(input())
for num in range(t):
    result=[]
    count=0
    for i in range(10):
        result.append(list(input()))
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j]=="X":
                if i==0 or j==0 or i==9 or j==9:
                    count+=1
                elif i==1 or j==1 or i==8 or j==8:
                    count+=2
                elif i==2 or j==2 or i==7 or j==7:
                    count+=3
                elif i==3 or j==3 or i==6 or j==6:
                    count+=4
                else:
                    count+=5
    print(count)
        