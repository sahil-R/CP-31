t=int(input())
for _ in range(t):
    (n,k)=list(map(int,input().split()))
    if n>k:
        total=0
        for i in range(min(n,k)):
            (bi,bc)=list(map(int,input().split()))
            total+=bc
        print(total)
    else:
        li={}
        for i in range(k):
            (bi,bc)=list(map(int,input().split()))
            if bi not in li:
                li[bi]=bc
            else:
                li[bi]+=bc
        ans=[li[x] for x in li.keys()]
        ans=sorted(ans,reverse=True)
        total=0
        # print(ans)
        for i in range(min(n,len(ans))):
            total+=ans[i]
        print(total)
