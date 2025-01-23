t=int(input())
for i in range(t):
    (target,forbidden)=list(map(int,input().split()))
    current=0
    jumps=0
    if target%forbidden==0:
        print(2)
        print(target-1,1)
    else:
        print(1)
        print(target)