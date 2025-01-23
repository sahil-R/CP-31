import math
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    minimum=math.inf
    flag=1
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            flag=0
        minimum=min(arr[i]-arr[i-1],minimum)
    if flag!=0:
        print((minimum//2)+1)
    else:
        print(0)