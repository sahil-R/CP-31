t=int(input())
for i in range(t):
    (a,b,n)=list(map(int,input().split()))
    buffers=list(map(int,input().split()))
    total=0
    total+=b
    for i in range(n):
        total+=min(1+buffers[i],a)
        total-=1
    print(total)        
