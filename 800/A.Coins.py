t=int(input())
for i in range(t):
    (n,k)=list(map(int,input().split()))
    if n%2==0:
        print("yes")
    else:
        if n%2==1 and k%2==0:
            print("no")
        else:
            print("yes")