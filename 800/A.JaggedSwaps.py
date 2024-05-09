t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    item=arr[0]
    minimum=min(arr[1:])
    for i in  arr:
        if i >n:
            print("NO")
    if item > minimum:
        print("NO")
    else:
        print("YES")