t=int(input())
for i in range(t):
    (a,b,c)=list(map(int,input().split()))
    ans=0
    if c%2==0:
        ans=2
    else:
        ans=1
    if a>b:
        ans=1
    if b>a:
        ans=2
    if ans==1:
        print("First")
    else:
        print("Second")
