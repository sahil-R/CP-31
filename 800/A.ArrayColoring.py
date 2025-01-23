t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    item=arr[0]
    if item%2==(sum(arr)-item)%2:
        print("YES")
    else:
        print("NO")