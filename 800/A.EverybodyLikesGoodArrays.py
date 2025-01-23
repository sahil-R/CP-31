t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(1,n):
        if arr[i]%2==arr[i-1]%2:
            count+=1
    print(count)
