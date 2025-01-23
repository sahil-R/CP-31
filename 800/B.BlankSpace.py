t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    length=0
    for i in range(len(arr)):
        if arr[i]==1:
            length=max(length,count)
            count=0
        else:
            count+=1
    length=max(length,count) 
    print(length)