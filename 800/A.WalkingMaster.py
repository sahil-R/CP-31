t=int(input())
for i in range(t):
    (a,b,c,d)=list(map(int,input().split()))
    if b>d:
        print(-1)
        continue
    else:
        steps=0
        height=abs(d-b)
        newx=a+height
        # print(height)
        if newx<c:
            print(-1)
            continue
        else:
            print(height+abs(c-newx))
