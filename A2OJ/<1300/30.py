n=int(input())
arr=list(map(int,input().split()))
t=int(input())
l=list(map(int,input().split()))
fwd=0
bwd=0
for _ in range(t):
    current=0
    item=l[_]
    for i in arr:
        if i!=item:
            current+=1
            fwd+=1
        else:
            fwd+=1
            current+=1
            bwd+=(n-current)+1
            break
print(fwd,bwd)    