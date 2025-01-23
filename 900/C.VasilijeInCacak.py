t=int(input())
for i in range(t):
    (n,k,x)=list(map(int,input().split()))
    min=k*(k+1)//2
    max=(n*(n+1)//2)-(n-k)*(n-k+1)//2
    if x>=min and x<=max:
        print("YES")
    else:
        print("NO")