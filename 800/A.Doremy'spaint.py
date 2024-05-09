t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if len(set(arr))==1:
        print("YES")
    else:
        if len(set(arr))>2:
            print("NO")
        else:
            a=arr.count(list(set(arr))[0])
            b=arr.count(list(set(arr))[1])
            if a==b or abs(a-b)==1:
                print("yes")
            else:
                print("no")