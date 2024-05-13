t=int(input())
for i in range(t):
    (n,m)=list(map(int,input().split()))
    s1=input()
    s2=input()
    flag=None
    count=0
    for i in range(6):
        if s2 in s1:
            flag=True
            flag=count
            break
        else:
            count+=1
            s1+=s1
    if flag==None:
        print(-1)
    else:
        print(flag)


