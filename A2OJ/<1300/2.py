# matrix=[]
for i in range(5):
    row=i//5
    col=i%5
    li=list(map(int,input().split()))
    for j in range(len(li)):
        if li[j]==1:
            print()
            chang=abs(2-i)+abs(2-j)
            print(chang)