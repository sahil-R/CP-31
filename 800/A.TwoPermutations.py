t=int(input())
for i in range(t):
    (n,a,b)=list(map(int,input().split()))
    if n==a and a==b:
        print("yes")
    elif n-(a+b)>1:
        print("yes")
    else:
        print("NO")