n=int(input())
gears=list(map(int,input().split()))
m=int(input())
_gears=list(map(int,input().split()))
ratio_count=0
ratio_total=None

for _ in range(n):
    for _1 in range(m):
        ratio=_gears[_1]/gears[_]
        # print(ratio,ratio_count,ratio_total)
        if ratio%1!=0:
            continue
        
        if ratio_total==None:
            ratio_total=ratio
            ratio_count=1
        elif ratio<ratio_total:
            continue
        elif ratio>ratio_total:
            ratio_total=ratio
            ratio_count=1
        elif ratio==ratio_total:
            ratio_count+=1
        else:
            ratio_count-=1
            if ratio_count==0:
                ratio_total=ratio
                ratio_count=1

print(ratio_count)
