t=int(input())
for i in range(t):
    (n,k)=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    if k in arr:
        print("YES")
    else:
        print("NO")
