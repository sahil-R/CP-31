t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    target=arr[0]
    if len(arr)==1:
        print(target)
    else:
        for item in arr[1:]:
            target^=item
        if n%2==1:
            print(target)
        else:
            if target==0:
                print(0)
            else:
                print(-1)